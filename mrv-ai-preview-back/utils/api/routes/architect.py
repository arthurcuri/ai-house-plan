"""
Rotas API para Área do Arquiteto
"""
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
import asyncio
import logging

from ...auth.middleware import get_current_active_user
from ...auth.models import User
from ...database.db_service import get_db
from ...database.architect_service import (
    create_personal_type,
    get_user_personal_types,
    get_personal_type_by_id,
    delete_personal_type,
    get_room_prompts,
    save_room_prompts,
    update_type_status
)
from ...core.architect.type_analyzer import analisar_fotos_e_gerar_prompts

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/arquiteto", tags=["arquiteto"])

# Constantes de validação
MAX_PHOTOS = 20
MIN_PHOTOS = 5
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_FORMATS = ["image/jpeg", "image/jpg", "image/png"]

def validar_fotos(fotos: List[UploadFile]) -> None:
    """Valida formato, tamanho e quantidade de fotos"""
    if len(fotos) < MIN_PHOTOS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Mínimo de {MIN_PHOTOS} fotos necessário"
        )
    if len(fotos) > MAX_PHOTOS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Máximo de {MAX_PHOTOS} fotos permitido"
        )
    
    for foto in fotos:
        if foto.content_type not in ALLOWED_FORMATS:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Formato {foto.content_type} não permitido. Use JPG ou PNG"
            )

async def processar_tipo_assincrono(
    tipo_id: int,
    fotos_bytes: List[bytes],
    nome_tipo: str,
    db: Session
):
    """Processa análise LLM em background"""
    try:
        # Analisar fotos e gerar prompts
        prompts_dict, analise_estilo = analisar_fotos_e_gerar_prompts(fotos_bytes, nome_tipo)
        
        # Salvar prompts no banco
        save_room_prompts(db, tipo_id, prompts_dict, analise_estilo)
        
        # Atualizar status
        update_type_status(db, tipo_id, "concluido", prompts_gerados=True)
        
        logger.info(f"Tipo {tipo_id} processado com sucesso")
    except Exception as e:
        logger.error(f"Erro ao processar tipo {tipo_id}: {e}")
        update_type_status(db, tipo_id, "erro", prompts_gerados=False)

@router.post("/tipos")
async def criar_tipo_pessoal(
    nome: str = Form(...),
    fotos: List[UploadFile] = File(...),
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Criar novo tipo pessoal"""
    # Validar fotos
    validar_fotos(fotos)
    
    # Ler bytes das fotos
    fotos_data = []
    for foto in fotos:
        foto_bytes = await foto.read()
        
        # Validar tamanho
        if len(foto_bytes) > MAX_FILE_SIZE:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Foto {foto.filename} excede 10MB"
            )
        
        formato = foto.content_type.split("/")[-1].upper()
        fotos_data.append((foto_bytes, formato, len(fotos_data)))
    
    # Criar tipo no banco
    tipo = create_personal_type(
        db=db,
        user_id=current_user.id,
        nome=nome,
        fotos_bytes=fotos_data
    )
    
    # Iniciar processamento assíncrono
    asyncio.create_task(
        processar_tipo_assincrono(
            tipo.id,
            [f[0] for f in fotos_data],
            nome,
            db
        )
    )
    
    return {
        "id": tipo.id,
        "nome": tipo.nome,
        "status": tipo.status,
        "created_at": tipo.created_at.isoformat()
    }

@router.get("/tipos")
async def listar_tipos_pessoais(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Listar tipos pessoais do usuário"""
    tipos = get_user_personal_types(db, current_user.id)
    
    return {
        "tipos": [
            {
                "id": t.id,
                "nome": t.nome,
                "status": t.status,
                "prompts_gerados": t.prompts_gerados,
                "created_at": t.created_at.isoformat(),
                "total_fotos": len(t.fotos_referencia)
            }
            for t in tipos
        ]
    }

@router.get("/tipos/{tipo_id}")
async def obter_tipo_pessoal(
    tipo_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Obter detalhes de um tipo pessoal"""
    tipo = get_personal_type_by_id(db, tipo_id, current_user.id)
    
    if not tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tipo pessoal não encontrado"
        )
    
    return {
        "id": tipo.id,
        "nome": tipo.nome,
        "descricao": tipo.descricao,
        "status": tipo.status,
        "prompts_gerados": tipo.prompts_gerados,
        "created_at": tipo.created_at.isoformat(),
        "total_fotos": len(tipo.fotos_referencia)
    }

@router.delete("/tipos/{tipo_id}")
async def deletar_tipo_pessoal(
    tipo_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Deletar tipo pessoal"""
    sucesso = delete_personal_type(db, tipo_id, current_user.id)
    
    if not sucesso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tipo pessoal não encontrado"
        )
    
    return {"success": True}

@router.get("/tipos/{tipo_id}/prompts")
async def obter_prompts_tipo(
    tipo_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Obter prompts de um tipo pessoal"""
    tipo = get_personal_type_by_id(db, tipo_id, current_user.id)
    
    if not tipo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tipo pessoal não encontrado"
        )
    
    prompts = get_room_prompts(db, tipo_id)
    
    return {"prompts": prompts}