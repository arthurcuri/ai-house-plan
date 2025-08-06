from fastapi import APIRouter, UploadFile, File, Form
from PIL import Image
import io
import numpy as np
import json
from main_api import reader
# from interpreter_plan import interpretar_planta_com_ocr  # Comentado temporariamente
from llm_factory import interpretar_planta_com_imagem  # Importação direta
from pipeline_generate_images import gerar_imagens_para_comodos
from json_utils import limpar_json_llm

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
        # Prompt estruturado para a LLM interpretar
        prompt = f"""Você é um assistente especialista em interpretação de plantas arquitetônicas residenciais.

Com base no seguinte texto extraído por OCR da planta:

{textos_ocr}

E considerando a imagem da planta fornecida, identifique com o máximo de precisão:

1. Quais são os cômodos presentes?
2. Quais são as dimensões aproximadas de cada um (em cm)?
3. Qual a localização relativa de cada cômodo (ex: 'superior esquerdo', 'centro', etc)?
4. Adicione também um campo opcional chamado "notas", com observações relevantes sobre limitações da planta, escala, possíveis ambiguidades, etc.

⚠️ Responda com **apenas o JSON bruto**, no seguinte formato:

{{"cômodos": [{{"nome": "...", "dimensões": {{"largura": ..., "comprimento": ...}}, "localização": "..."}}], "notas": ["..."]}}

❌ **Não use expressões matemáticas** como "122 + 120". Faça o cálculo e informe apenas o valor numérico final.

❌ Não inclua explicações, markdown ou campos extras."""

        interpretacao_raw = interpretar_planta_com_imagem(prompt, contents)
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