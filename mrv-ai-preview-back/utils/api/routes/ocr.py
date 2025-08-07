from fastapi import APIRouter, UploadFile, File, Form
from PIL import Image
import io
import numpy as np
from core.ocr.ocr_service import reader
import sys
from pathlib import Path

# Adicionar utils ao path para imports
current_dir = Path(__file__).parent.parent.parent
sys.path.insert(0, str(current_dir))

from core.ai import interpreter_plan

router = APIRouter()

@router.post("/ocr")
async def processar_planta(file: UploadFile = File(...), tipo: str = Form(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    image_np = np.array(image)

    # EasyOCR retorna lista de blocos [bbox, texto, confiança]textos_extraidos
    result = reader.readtext(image_np)

    # Extrair só os textos (ou mais estrutura se quiser)
    textos_extraidos = [r[1] for r in result]

    # ✅ NOVA INTEGRAÇÃO: Chamar o interpretador com o OCR e tipo de apartamento
    try:
        interpretacao_llm = interpreter_plan.interpretar_planta_com_ocr(contents, textos_extraidos, tipo)
        
        return {
            "interpretacao_llm": interpretacao_llm,
            "tipo": tipo
        }
    except Exception as e:
        # Se a LLM falhar, retorna erro
        return {
            "interpretacao_llm": f"Erro na interpretação: {str(e)}",
            "tipo": tipo
        }
