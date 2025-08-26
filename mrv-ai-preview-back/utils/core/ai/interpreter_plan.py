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
    prompt = f"""You are a specialist assistant in interpreting residential architectural floor plans.

            Based on the following text extracted by OCR from the plan:

            {texto_ocr}

            And considering the provided floor plan image, identify with maximum accuracy:

            1. Which rooms are present?
            2. What are the approximate dimensions of each (in cm)?
            3. What is the relative location of each room (e.g., 'upper left', 'center', etc.)?
            4. Also add an optional field called "notas" for each room containing:
            - Relevant observations about plan limitations, scale, possible ambiguities, etc.
            - Detailed description of the furniture layout within each room.
            - Shape of the furniture and its relative size compared to the rest of the room (for example: "sofa occupies half the length of the north wall", "small round table in the center", "queen bed against the east wall").
            - The maximum possible description of each piece of furniture present, so that the 3D model generation is accurate and realistic.


           Return **only the raw JSON**, exactly in this schema (keys MUST remain in Portuguese):
        {{"cômodos": [{{"nome": "...", "dimensões": {{"largura": ..., "comprimento": ...}}, "localização": "...", "notas": "..."}}]}}

        STRICT RULES:
        - All JSON keys MUST be exactly these in Portuguese: "cômodos", "nome", "dimensões", "largura", "comprimento", "localização", "notas".
        - The content/value of "notas" MUST be written in ENGLISH (translate if OCR is in another language).
        - Dimensions must be numeric values in centimeters (integers or decimals), without units in the numbers.
        - Do NOT use mathematical expressions (e.g., "122 + 120"); provide only the final numeric value.
        - Do NOT include explanations, markdown, code fences, or extra fields."""


    # Chamada para a LLM
    resposta = interpretar_planta_com_imagem(prompt, image_bytes)
    
    return resposta
