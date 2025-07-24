import google.generativeai as genai
from dotenv import load_dotenv
import os
import requests


# Carregar variáveis do .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY_LUCAS")
genai.configure(api_key=GEMINI_API_KEY)

# Modelos específicos por funcionalidade
modelo_texto = genai.GenerativeModel("gemini-2.5-flash")
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
    contents = [prompt]
    if image_bytes:
        # modelo multimodal
        contents.append({"mime_type": "image/jpeg", "data": image_bytes})
    response = genai.Client().models.generate_content(
        model="gemini-2.0-flash-preview-image-generation",
        contents=contents,
        config=genai.types.GenerateContentConfig(response_modalities=["TEXT", "IMAGE"])
    )
    parts = response.candidates[0].content.parts
    for part in parts:
        if part.inline_data is not None:
            return part.inline_data.data
    raise RuntimeError("Nenhuma imagem gerada.")


def interpretar_planta_com_imagem(prompt: str, image_bytes: bytes) -> str:
    contents = [
        {"mime_type": "image/jpeg", "data": image_bytes},
        {"text": prompt}
    ]
    response = modelo_multimodal.generate_content(contents)
    return response.text