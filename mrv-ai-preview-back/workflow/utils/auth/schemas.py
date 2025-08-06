from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional
import re

class LoginRequest(BaseModel):
    email: EmailStr = Field(..., description="Email do usuário")
    senha: str = Field(..., min_length=6, max_length=100, description="Senha do usuário")

class RegisterRequest(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100, description="Nome completo do usuário")
    email: EmailStr = Field(..., description="Email do usuário")
    senha: str = Field(..., min_length=6, max_length=100, description="Senha do usuário")
    
    @validator('nome')
    def validate_nome(cls, v):
        if not v or not v.strip():
            raise ValueError('Nome não pode estar vazio')
        if len(v.strip()) < 2:
            raise ValueError('Nome deve ter pelo menos 2 caracteres')
        return v.strip()
    
    # Simplificando a validação de senha para desenvolvimento
    @validator('senha')
    def validate_senha(cls, v):
        if len(v) < 6:
            raise ValueError('Senha deve ter pelo menos 6 caracteres')
        if len(v) > 100:
            raise ValueError('Senha muito longa')
        return v

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int = Field(default=3600, description="Tempo de expiração em segundos")

class UserResponse(BaseModel):
    id: int
    nome: str
    email: str
    
    class Config:
        from_attributes = True 