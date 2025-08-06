import easyocr
from PIL import Image
import io
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import logging
from ocr_reader import reader
# from interpreter_plan import interpretar_planta_com_ocr  # Comentado temporariamente
from llm_factory import interpretar_planta_com_imagem  # Importação direta
from routes.generate_images_api import router as imagens_router
from auth.routes import router as auth_router
from auth.models import Base
from db import engine, init_db
from config import settings

# Configurar logging simples para desenvolvimento
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Inicializar banco de dados SQLite
try:
    init_db()
    logger.info("Banco SQLite inicializado com sucesso")
except Exception as e:
    logger.error(f"Erro ao inicializar banco de dados SQLite: {e}")

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    description="API para processamento de plantas baixas com IA - Desenvolvimento",
    docs_url="/docs",  # Sempre disponível em desenvolvimento
    redoc_url="/redoc",
)

# CORS simples para desenvolvimento
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


@app.post("/ocr")
async def processar_planta(file: UploadFile = File(...), tipo: str = Form(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    image_np = np.array(image)

    # EasyOCR retorna lista de blocos [bbox, texto, confiança]textos_extraidos
    result = reader.readtext(image_np)

    # Extrair só os textos (ou mais estrutura se quiser)
    textos_extraidos = [r[1] for r in result]

    # ✅ NOVA INTEGRAÇÃO: Chamar o interpretador diretamente com o OCR e tipo de apartamento
    try:
        # Prompt estruturado para a LLM interpretar
        prompt = f"""Você é um assistente especialista em interpretação de plantas arquitetônicas residenciais.

Com base no seguinte texto extraído por OCR da planta:

{textos_extraidos}

E considerando a imagem da planta fornecida, identifique com o máximo de precisão:

1. Quais são os cômodos presentes?
2. Quais são as dimensões aproximadas de cada um (em cm)?
3. Qual a localização relativa de cada cômodo (ex: 'superior esquerdo', 'centro', etc)?
4. Adicione também um campo opcional chamado "notas", com observações relevantes sobre limitações da planta, escala, possíveis ambiguidades, etc.

⚠️ Responda com **apenas o JSON bruto**, no seguinte formato:

{{"cômodos": [{{"nome": "...", "dimensões": {{"largura": ..., "comprimento": ...}}, "localização": "..."}}], "notas": ["..."]}}

❌ **Não use expressões matemáticas** como "122 + 120". Faça o cálculo e informe apenas o valor numérico final.

❌ Não inclua explicações, markdown ou campos extras."""

        interpretacao_llm = interpretar_planta_com_imagem(prompt, contents)
        
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
app.include_router(auth_router)