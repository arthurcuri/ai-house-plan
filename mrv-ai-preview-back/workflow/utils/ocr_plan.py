import easyocr
from PIL import Image
import io
from fastapi import FastAPI, UploadFile, File
import numpy as np


app = FastAPI()
reader = easyocr.Reader(['pt', 'en'], gpu=False)  # você pode ativar gpu=True se quiser



@app.post("/ocr")
async def processar_planta(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    image_np = np.array(image)

    # EasyOCR retorna lista de blocos [bbox, texto, confiança]
    result = reader.readtext(image_np)

    # Extrair só os textos (ou mais estrutura se quiser)
    textos_extraidos = [r[1] for r in result]

    return {"texto_extraido": textos_extraidos}