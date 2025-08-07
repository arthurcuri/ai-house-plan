from core.ai.gemini_service import interpretar_planta_com_imagem
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
    
    # Prompt estruturado para a LLM interpretar
    prompt = f"""Você é um assistente especialista em interpretação de plantas arquitetônicas residenciais.

Com base no seguinte texto extraído por OCR da planta:

{texto_ocr}

E considerando a imagem da planta fornecida, identifique com o máximo de precisão:

1. Quais são os cômodos presentes?
2. Quais são as dimensões aproximadas de cada um (em cm)?
3. Qual a localização relativa de cada cômodo (ex: 'superior esquerdo', 'centro', etc)?
4. Adicione também um campo opcional chamado "notas", com observações relevantes sobre limitações da planta, escala, possíveis ambiguidades, etc.

⚠️ Responda com **apenas o JSON bruto**, no seguinte formato:

{{"cômodos": [{{"nome": "...", "dimensões": {{"largura": ..., "comprimento": ...}}, "localização": "..."}}], "notas": ["..."]}}

❌ **Não use expressões matemáticas** como "122 + 120". Faça o cálculo e informe apenas o valor numérico final.

❌ Não inclua explicações, markdown ou campos extras."""

    # Chamada para a LLM
    resposta = interpretar_planta_com_imagem(prompt, image_bytes)
    
    return resposta
