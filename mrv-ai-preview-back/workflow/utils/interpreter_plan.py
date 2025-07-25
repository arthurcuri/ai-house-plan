from llm_factory import interpretar_planta_com_imagem
import io
from PIL import Image

def interpretar_planta_com_ocr(image_bytes: bytes, texto_ocr: list, tipo_apartamento: str):
    """
    Interpreta uma planta baixa usando OCR e LLM
    
    Args:
        image_bytes: Bytes da imagem da planta
        texto_ocr: Lista de textos extraídos por OCR (valores reais da planta)
        tipo_apartamento: Tipo do apartamento (class, eco, bio, essential)
    
    Returns:
        Resposta da LLM interpretando a planta
    """
    
    # ✅ Prompt estruturado para a LLM interpretar (SEM tipo de apartamento)
    prompt = f"""
Você é um assistente especialista em interpretação de plantas arquitetônicas residenciais.

Com base no seguinte texto extraído por OCR da planta:

{texto_ocr}

E considerando a imagem da planta fornecida, identifique com o máximo de precisão:

1. Quais são os cômodos presentes?
2. Quais são as dimensões aproximadas de cada um (em cm)?
3. Qual a localização relativa de cada cômodo (ex: 'superior esquerdo', 'centro', etc)?

Responda em formato JSON estruturado. Seja preciso e conciso.
"""

    # ✅ Chamada para a LLM
    resposta = interpretar_planta_com_imagem(prompt, image_bytes)
    
    return resposta
