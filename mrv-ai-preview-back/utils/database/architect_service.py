"""
Serviço para operações de banco de dados relacionadas a tipos pessoais
"""
from sqlalchemy.orm import Session
from typing import List, Dict, Optional
from datetime import datetime
from .architect_models import ArchitectPersonalType, TypeReferencePhoto, TypeRoomPrompt

def create_personal_type(
    db: Session,
    user_id: int,
    nome: str,
    fotos_bytes: List[tuple],  # [(bytes, formato, ordem), ...]
    descricao: str = None
) -> ArchitectPersonalType:
    """Cria um novo tipo pessoal e salva as fotos"""
    tipo = ArchitectPersonalType(
        user_id=user_id,
        nome=nome,
        descricao=descricao,
        status="processando",
        prompts_gerados=False
    )
    db.add(tipo)
    db.flush()  # Para obter o ID
    
    # Salvar cada foto
    for ordem, (foto_bytes, formato, _) in enumerate(fotos_bytes, start=1):
        foto = TypeReferencePhoto(
            tipo_id=tipo.id,
            foto_data=foto_bytes,
            tamanho_bytes=len(foto_bytes),
            formato=formato.upper(),
            ordem=ordem
        )
        db.add(foto)
    
    db.commit()
    db.refresh(tipo)
    return tipo

def get_user_personal_types(db: Session, user_id: int) -> List[ArchitectPersonalType]:
    """Lista todos os tipos pessoais do usuário"""
    return db.query(ArchitectPersonalType).filter(
        ArchitectPersonalType.user_id == user_id
    ).order_by(ArchitectPersonalType.created_at.desc()).all()

def get_personal_type_by_id(
    db: Session, 
    tipo_id: int, 
    user_id: int
) -> Optional[ArchitectPersonalType]:
    """Busca tipo por ID (com validação de ownership)"""
    return db.query(ArchitectPersonalType).filter(
        ArchitectPersonalType.id == tipo_id,
        ArchitectPersonalType.user_id == user_id
    ).first()

def delete_personal_type(db: Session, tipo_id: int, user_id: int) -> bool:
    """Deleta tipo e todas as fotos/prompts relacionados (cascade)"""
    tipo = get_personal_type_by_id(db, tipo_id, user_id)
    if not tipo:
        return False
    
    db.delete(tipo)
    db.commit()
    return True

def get_room_prompts(db: Session, tipo_id: int) -> Dict[str, str]:
    """Retorna dict {tipo_comodo: prompt_personalizado}"""
    prompts = db.query(TypeRoomPrompt).filter(
        TypeRoomPrompt.tipo_id == tipo_id
    ).all()
    
    return {p.tipo_comodo: p.prompt_personalizado for p in prompts}

def save_room_prompts(
    db: Session, 
    tipo_id: int, 
    prompts_dict: Dict[str, str],
    analise_estilo: str = None
):
    """Salva prompts gerados pela LLM"""
    for tipo_comodo, prompt in prompts_dict.items():
        # Verificar se já existe
        existing = db.query(TypeRoomPrompt).filter(
            TypeRoomPrompt.tipo_id == tipo_id,
            TypeRoomPrompt.tipo_comodo == tipo_comodo
        ).first()
        
        if existing:
            existing.prompt_personalizado = prompt
            if analise_estilo:
                existing.analise_estilo = analise_estilo
        else:
            prompt_obj = TypeRoomPrompt(
                tipo_id=tipo_id,
                tipo_comodo=tipo_comodo,
                prompt_personalizado=prompt,
                analise_estilo=analise_estilo
            )
            db.add(prompt_obj)
    
    db.commit()

def update_type_status(
    db: Session, 
    tipo_id: int, 
    status: str, 
    prompts_gerados: bool = False
):
    """Atualiza status do tipo"""
    tipo = db.query(ArchitectPersonalType).filter(
        ArchitectPersonalType.id == tipo_id
    ).first()
    
    if tipo:
        tipo.status = status
        tipo.prompts_gerados = prompts_gerados
        tipo.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(tipo)
    
    return tipo