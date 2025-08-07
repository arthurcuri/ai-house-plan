from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from .utils import decode_access_token
from .models import get_user_by_email, User
from database.db_service import get_db
from typing import Optional
import logging

logger = logging.getLogger(__name__)

# Configurar esquema de segurança
security = HTTPBearer(auto_error=False)

def get_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    """
    Dependency para obter o usuário atual através do token JWT
    """
    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token de acesso necessário",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Decodificar token
    payload = decode_access_token(credentials.credentials)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Obter email do payload
    email: str = payload.get("sub")
    if not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Buscar usuário no banco
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não encontrado",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user

def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    """
    Dependency para obter usuário ativo (pode ser expandida com status de usuário)
    """
    # Aqui você pode adicionar verificações adicionais como usuário ativo, verificado, etc.
    return current_user

# Dependency opcional para rotas que podem ou não ter autenticação
def get_current_user_optional(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
    db: Session = Depends(get_db)
) -> Optional[User]:
    """
    Dependency opcional para obter o usuário atual (não obrigatório)
    """
    if not credentials:
        return None
    
    try:
        return get_current_user(credentials, db)
    except HTTPException:
        return None
