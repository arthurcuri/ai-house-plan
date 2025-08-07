from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .schemas import LoginRequest, RegisterRequest, TokenResponse
from .models import authenticate_user, get_user_by_email, User
from .utils import create_access_token, hash_password
from database.db_service import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, data.email, data.senha)
    if not user:
        raise HTTPException(status_code=401, detail="Email ou senha incorretos.")
    token = create_access_token({"sub": user.email, "nome": user.nome})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/register", response_model=TokenResponse)
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    if get_user_by_email(db, data.email):
        raise HTTPException(status_code=400, detail="Usuário já existe.")
    novo_usuario = User(
        nome=data.nome,
        email=data.email,
        senha_hashed=hash_password(data.senha)
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    token = create_access_token({"sub": novo_usuario.email, "nome": novo_usuario.nome})
    return {"access_token": token, "token_type": "bearer"}