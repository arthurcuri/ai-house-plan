from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from .schemas import LoginRequest, RegisterRequest, TokenResponse, UserResponse
from .models import authenticate_user, get_user_by_email, User
from .utils import create_access_token, hash_password
from .middleware import get_current_user
from db import get_db  # Import absoluto
import logging

# Configurar logging
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/auth", tags=["authentication"])

@router.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    """Realizar login do usuário"""
    try:
        # Authenticar usuário
        user = authenticate_user(db, data.email, data.senha)
        if not user:
            logger.warning(f"Tentativa de login falhada para email: {data.email}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Email ou senha incorretos",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Criar token
        access_token = create_access_token(
            data={"sub": user.email, "nome": user.nome, "user_id": user.id}
        )
        
        logger.info(f"Login bem-sucedido para o usuário: {user.email}")
        return {
            "access_token": access_token, 
            "token_type": "bearer",
            "expires_in": 3600
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro interno no login: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro interno do servidor"
        )

@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    """Registrar novo usuário"""
    try:
        # Verificar se usuário já existe
        if get_user_by_email(db, data.email):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Usuário já existe com este email"
            )
        
        # Criar novo usuário
        novo_usuario = User(
            nome=data.nome,
            email=data.email.lower(),  # Normalizar email
            senha_hashed=hash_password(data.senha)
        )
        
        db.add(novo_usuario)
        db.commit()
        db.refresh(novo_usuario)
        
        # Criar token para o novo usuário
        access_token = create_access_token(
            data={"sub": novo_usuario.email, "nome": novo_usuario.nome, "user_id": novo_usuario.id}
        )
        
        logger.info(f"Novo usuário registrado: {novo_usuario.email}")
        return {
            "access_token": access_token, 
            "token_type": "bearer",
            "expires_in": 3600
        }
        
    except HTTPException:
        raise
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Usuário já existe com este email"
        )
    except Exception as e:
        db.rollback()
        logger.error(f"Erro interno no registro: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro interno do servidor"
        )

@router.get("/me", response_model=UserResponse)
def get_current_user_info(current_user: User = Depends(get_current_user)):
    """Obter informações do usuário atual"""
    return current_user

@router.post("/validate-token")
def validate_token(current_user: User = Depends(get_current_user)):
    """Validar se o token é válido"""
    return {
        "valid": True,
        "user": {
            "id": current_user.id,
            "nome": current_user.nome,
            "email": current_user.email
        }
    }