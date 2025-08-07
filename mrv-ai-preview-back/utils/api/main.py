import easyocr
from PIL import Image
import io
from fastapi import FastAPI, UploadFile, File, Form
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

# Imports das rotas organizadas
from api.routes.image_generation import router as imagens_router
from api.routes.ocr import router as ocr_router
from auth.routes import router as auth_router
from auth.models import Base
from database.db_service import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui as 4 rotas organizadas
app.include_router(ocr_router)           # POST /ocr
app.include_router(imagens_router)       # POST /gerar-imagens  
app.include_router(auth_router)          # POST /auth/login, /auth/register