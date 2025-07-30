import easyocr
from PIL import Image
import io
from fastapi import FastAPI, UploadFile, File, Form
import numpy as np
from ocr_reader import reader
from interpreter_plan import interpretar_planta_com_ocr
from routes.generate_images_api import router as imagens_router

app = FastAPI()

@app.post("/ocr")
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
        interpretacao_llm = interpretar_planta_com_ocr(contents, textos_extraidos, tipo)
        
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
    
# Inclui as demais rotas
app.include_router(imagens_router)