import google.generativeai as genai
from dotenv import load_dotenv
import os

# Lógica usando GEMINI
# Carregar variáveis do .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY_LUCAS")
genai.configure(api_key=GEMINI_API_KEY)

# Modelos específicos por funcionalidade
modelo_texto = genai.GenerativeModel("gemini-1.5-flash")
modelo_imagem = genai.GenerativeModel("gemini-1.5-flash")  # Usando flash para imagens também
modelo_multimodal = genai.GenerativeModel("gemini-1.5-flash")


def interpretar_texto(prompt: str, history: list[dict] = None) -> str:
    """
    Usa modelo de texto para interpretação ou análise (ex: OCR).
    """
    try:
        if history:
            response = modelo_texto.chat(
                history=history + [{"role": "user", "parts": [prompt]}]
            )
            return response.last.choice.content.text
        else:
            response = modelo_texto.generate_content(prompt)
            return response.text
    except Exception as e:
        raise RuntimeError(f"Erro na interpretação de texto: {str(e)}")


def gerar_imagem(prompt: str, image_bytes: bytes = None) -> bytes:
    """
    Para fins de demonstração, retorna dados de imagem simulados.
    Em uma implementação real, integraria com APIs de geração de imagem.
    """
    try:
        # Por enquanto, retorna dados simulados
        # A geração real de imagens seria implementada aqui
        return b"placeholder_image_data"
        
    except Exception as e:
        raise RuntimeError(f"Erro ao gerar imagem: {str(e)}")


def interpretar_planta_com_imagem(prompt: str, image_bytes: bytes) -> str:
    """
    Interpreta uma planta baixa usando modelo multimodal do Gemini
    """
    try:
        # Preparar conteúdo multimodal
        contents = [
            {"mime_type": "image/jpeg", "data": image_bytes},
            {"text": prompt}
        ]
        response = modelo_multimodal.generate_content(contents)
        return response.text
    except Exception as e:
        raise RuntimeError(f"Erro na interpretação da planta: {str(e)}")


def classificar_tipo_comodo(prompt: str) -> str:
    """
    Classifica o tipo de cômodo com base em descrição textual, usando o modelo de texto Gemini.
    
    Retorna apenas a string com o tipo (ex: 'quarto_casal', 'sala', etc.).
    """
    try:
        response = modelo_texto.generate_content(prompt)
        return response.text.strip().lower()
    except Exception as e:
        raise RuntimeError(f"Erro na classificação de cômodo: {str(e)}")

    