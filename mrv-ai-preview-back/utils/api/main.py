import easyocr
from PIL import Image
import io
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
import os

from pathlib import Path

# Imports das rotas organizadas
from .routes.image_generation import router as imagens_router
from .routes.ocr import router as ocr_router
from ..auth.routes import router as auth_router
from ..auth.models import Base
from ..database.db_service import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Diretório "generated_images" dentro do projeto
BASE_DIR = Path(__file__).resolve().parent.parent  # sobe para a raiz do back-end
IMAGES_OUTPUT_DIR = BASE_DIR / "generated_images"
IMAGES_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


app.mount("/imagens", StaticFiles(directory=IMAGES_OUTPUT_DIR), name="imagens")

# Inclui as rotas organizadas
app.include_router(ocr_router)           # POST /ocr
app.include_router(imagens_router)       # POST /gerar-imagens (unificada)
app.include_router(auth_router)          # POST /auth/login, /auth/register