from fastapi import APIRouter, UploadFile, File, Form
from PIL import Image
import io
import numpy as np
import json
from core.ocr.ocr_service import reader
from core.ai import interpreter_plan
from core.image_generation.image_service import gerar_imagens_para_comodos
from shared.json_utils import limpar_json_llm

router = APIRouter()

@router.post("/gerar-imagens")
async def gerar_imagens(file: UploadFile = File(...), tipo: str = Form(...)):
    """
    Gera imagens 3D de cada cômodo da planta enviada, com base no padrão de acabamento informado.
    """
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    image_np = np.array(image)

    # ✅ OCR
    result = reader.readtext(image_np)
    textos_ocr = [r[1] for r in result]

    # ✅ Interpretação da planta via LLM
    try:
        interpretacao_raw = interpreter_plan.interpretar_planta_com_ocr(contents, textos_ocr, tipo)
        dados = limpar_json_llm(interpretacao_raw)
    except Exception as e:
        return {
            "erro": f"Erro ao interpretar a planta ou ao decodificar JSON: {str(e)}",
            "interpretacao_raw": interpretacao_raw if 'interpretacao_raw' in locals() else None
        }

    comodos = dados.get("cômodos") or dados.get("comodos")  # aceitar ambos formatos

    if not comodos:
        return {"erro": "Nenhum cômodo encontrado na interpretação da planta."}

    # ✅ Geração das imagens
    imagens = gerar_imagens_para_comodos(comodos, contents)

    return {
        "tipo": tipo,
        "quantidade_comodos": len(comodos),
        "resultado": imagens
    }
