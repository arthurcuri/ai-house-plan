# from google.generativeai import GenerativeModel  # ❌ Comentado para evitar erro
from dotenv import load_dotenv
import os
import requests

# Carregar variáveis do .env
load_dotenv()

# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY_LUCAS")
# genai.configure(api_key=GEMINI_API_KEY)

# # Modelos específicos por funcionalidade (Gemini) — DESATIVADOS
# modelo_texto = genai.GenerativeModel("gemini-2.5-flash")
# modelo_imagem = genai.GenerativeModel("gemini-2.0-flash-preview-image-generation")
# modelo_multimodal = genai.GenerativeModel("gemini-1.5-pro")

# 🔁 Hugging Face API key
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")  # Adicione isso ao seu .env
HEADERS = {
    "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
    "Content-Type": "application/json"
}


def interpretar_texto(prompt: str, history: list[dict] = None) -> str:
    """
    Usa modelo Hugging Face para interpretação textual.
    """
    response = requests.post(
        "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct",
        headers=HEADERS,
        json={"inputs": prompt}
    )
    return response.json()[0]['generated_text'].strip()


def classificar_tipo_comodo(prompt: str) -> str:
    """
    Classifica o tipo de cômodo com base em descrição textual.
    """
    return interpretar_texto(prompt).lower()


def gerar_imagem(prompt: str, image_bytes: bytes = None) -> bytes:
    """
    Gera imagem a partir de prompt usando Stable Diffusion (sem multimodal).
    Retorna bytes da imagem.
    """
    response = requests.post(
        "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2",
        headers=HEADERS,
        json={"inputs": prompt}
    )
    return response.content  # Retorna imagem gerada


def interpretar_planta_com_imagem(prompt: str, image_bytes: bytes) -> str:
    """
    Interpretação multimodal desativada (por enquanto). Usa apenas texto.
    """
    return interpretar_texto(prompt)  # Usa modelo textual apenas como fallback
