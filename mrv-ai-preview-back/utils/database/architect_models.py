"""
Modelos de dados para tipos pessoais de arquitetura
"""
from sqlalchemy import Column, Integer, String, Text, DateTime, BLOB, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .db_service import Base

class ArchitectPersonalType(Base):
    __tablename__ = "architect_personal_types"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    nome = Column(String(200), nullable=False)
    descricao = Column(Text, nullable=True)
    
    status = Column(String(50), default="processando")  # processando, concluido, erro
    prompts_gerados = Column(Boolean, default=False)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    fotos_referencia = relationship("TypeReferencePhoto", back_populates="tipo", cascade="all, delete-orphan")
    prompts_comodos = relationship("TypeRoomPrompt", back_populates="tipo", cascade="all, delete-orphan")

class TypeReferencePhoto(Base):
    __tablename__ = "type_reference_photos"
    
    id = Column(Integer, primary_key=True, index=True)
    tipo_id = Column(Integer, ForeignKey("architect_personal_types.id"), nullable=False, index=True)
    
    foto_data = Column(BLOB, nullable=False)
    tamanho_bytes = Column(Integer, nullable=False)
    formato = Column(String(10))  # JPG, PNG
    ordem = Column(Integer, default=0)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    tipo = relationship("ArchitectPersonalType", back_populates="fotos_referencia")

class TypeRoomPrompt(Base):
    __tablename__ = "type_room_prompts"
    
    id = Column(Integer, primary_key=True, index=True)
    tipo_id = Column(Integer, ForeignKey("architect_personal_types.id"), nullable=False, index=True)
    
    tipo_comodo = Column(String(100), nullable=False, index=True)
    prompt_personalizado = Column(Text, nullable=False)
    analise_estilo = Column(Text, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    tipo = relationship("ArchitectPersonalType", back_populates="prompts_comodos")