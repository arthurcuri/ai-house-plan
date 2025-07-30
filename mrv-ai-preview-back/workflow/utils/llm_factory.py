import google.generativeai as genai
#from google import genai
from google.genai import types
from google.generativeai.types import generation_types
from google.generativeai import GenerativeModel
from dotenv import load_dotenv
import os
import requests



 # Lógica usando GEMINI em comentario
# Carregar variáveis do .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY_LUCAS")
genai.configure(api_key=GEMINI_API_KEY)

# Modelos específicos por funcionalidade
modelo_texto = genai.GenerativeModel("gemini-1.5-flash")
modelo_imagem = genai.GenerativeModel("gemini-2.0-flash-preview-image-generation")
modelo_multimodal = genai.GenerativeModel("gemini-1.5-flash")


def interpretar_texto(prompt: str, history: list[dict] = None) -> str:
    """
    Usa modelo de texto para interpretação ou análise (ex: OCR).
    """
    config = {}
    if history:
        response = modelo_texto.chat(  # conversa com histórico
            history=history + [{"role": "user", "parts": [prompt]}]
        )
        return response.last.choice.content.text
    else:
        response = modelo_texto.generate_content(prompt)
        return response.text

def gerar_imagem(prompt: str, image_bytes: bytes = None) -> bytes:
    """
    Gera ou edita imagem 3D com modelo Gemini 2.0 Flash Preview Image Generation.
    Pode receber prompt apenas ou prompt + imagem de base para edição.
    Retorna bytes da imagem gerada.
    """
    contents = [{"text": prompt}]
    if image_bytes:
        contents.append({"mime_type": "image/jpeg", "data": image_bytes})

    client = genai.Client(api_key=GEMINI_API_KEY)
    response = client.models.generate_content(
        model="gemini-2.0-flash-preview-image-generation",
        contents=contents,
        config=types.GenerateContentConfig(
            response_modalities=["Text", "IMAGE"]
        )
    )


    # ✅ Pega a imagem da resposta
    for part in response.parts:
        if hasattr(part, "inline_data") and part.inline_data is not None:
            return part.inline_data.data

    raise RuntimeError("Nenhuma imagem foi gerada pela LLM.")



def interpretar_planta_com_imagem(prompt: str, image_bytes: bytes) -> str:
    contents = [
        {"mime_type": "image/jpeg", "data": image_bytes},
        {"text": prompt}
    ]
    response = modelo_multimodal.generate_content(contents)
    return response.text



def classificar_tipo_comodo(prompt: str) -> str:
    """
    Classifica o tipo de cômodo com base em descrição textual, usando o modelo de texto Gemini.
    
    Retorna apenas a string com o tipo (ex: 'quarto_casal', 'sala', etc.).
    """
    response = modelo_texto.generate_content(prompt)
    return response.text.strip().lower()

    