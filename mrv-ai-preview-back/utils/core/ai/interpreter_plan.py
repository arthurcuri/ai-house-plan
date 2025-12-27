from core.ai.gemini_service import interpretar_planta_com_imagem
import io
from PIL import Image


from core.ai.gemini_service import interpretar_planta_com_imagem_structured
from core.ai.schemas import InterpretacaoPlanta, Comodo, Dimensoes, ContextoGeral
import logging

def interpretar_planta_com_ocr(image_bytes: bytes, texto_ocr: list, tipo_apartamento: str = None, tipo_pessoal_nome: str = None):
    """
    Interpreta uma planta baixa usando OCR e LLM com Structured Output.
    
    Args:
        image_bytes: Bytes da imagem da planta
        texto_ocr: Lista de textos extraídos por OCR
        tipo_apartamento: Tipo do apartamento (essential, eco, bio, class)
    
    Returns:
        dict: Dados estruturados e validados da interpretação
    """

     # Validar que pelo menos um tipo foi fornecido
    if not tipo_apartamento and not tipo_pessoal_nome:
        raise ValueError("É necessário fornecer 'tipo_apartamento' ou 'tipo_pessoal_nome'")

    # Determinar o tipo para o contexto
    if tipo_pessoal_nome:
        tipo_contexto = f"Tipo pessoal: {tipo_pessoal_nome}"
    else:
        tipo_contexto = f"Tipo padrão MRV: {tipo_apartamento}"
    
    # Prompt estruturado para a LLM interpretar
    prompt = f"""You are an expert architectural analyst specializing in residential floor plans.

            Based on the OCR text extracted from the plan:
            {texto_ocr}

            And analyzing the provided floor plan image, perform a COMPREHENSIVE analysis:

            1. Identify ALL rooms present
            2. For EACH room, provide:
            - Exact name (in Portuguese)
            - Dimensions in BOTH centimeters and meters
            - Area in m² (calculate: largura_m x comprimento_m)
            - Room type classification from the allowed enum
            - Shape/proportion: "retangular alongado", "quadrado", "retangular estreito", "L-shaped", etc.
            - Relative position: "upper left", "center", "north", "south", etc.
            - Fixed elements: windows, doors, columns (list with positions)
            - Furniture layout suggestion: based on dimensions, suggest optimal layout
            - Scale context: "maior cômodo", "menor cômodo", "cômodo médio" compared to others
            - Furniture positioning details: exact positions from walls in cm, furniture sizes relative to room

            3. Overall context:
            - Apartment type: {tipo_contexto}
            - Solar orientation (if visible): north, south, east, west
            - Circulation flow: linear, circular, etc.
            - Total area estimate

            IMPORTANT:
            - Calculate area_m2 = largura_m × comprimento_m for each room
            - Convert dimensions: largura_m = largura_cm / 100
            - Furniture positioning must include exact distances from walls
            - Furniture sizes must be realistic and proportional to room dimensions
            - "notas" field must be in ENGLISH with detailed layout descriptions
            """


    try:
        #usar structured outputs
        dados = interpretar_planta_com_imagem_structured(
            prompt = prompt,
            image_bytes = image_bytes,
            schema =  InterpretacaoPlanta
        )

        return dados

    except Exception as e:
        logging.error(f"Erro na interpretação estruturada: {e}")
        raise RuntimeError(f"Erro ao interpretar planta: {e}")