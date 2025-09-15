"""
Serviço para gerenciamento de imagens no banco SQLite
Estrutura hierárquica: Usuário → Plantas → Sessões → Imagens
"""

import hashlib
import time
from typing import Optional, List, Dict, Any
from sqlalchemy.orm import Session

from .image_models import (
    UserPlanta, ImageSession, GeneratedImage,
    create_user_planta, create_image_session, save_generated_image,
    get_user_plantas, get_planta_sessions, get_session_images, 
    get_user_all_images, update_session_progress
)
from .db_service import SessionLocal


class ImageDatabaseService:
    """
    Serviço para operações de imagens no banco de dados
    """
    
    @staticmethod
    def create_planta_and_session(user_id: int, tipo_apartamento: str, 
                                 planta_bytes: bytes, comodos_data: List[Dict],
                                 nome_planta: str = None, ocr_texto: str = None,
                                 interpretacao_llm: str = None) -> tuple[UserPlanta, ImageSession]:
        """
        Cria uma nova planta e sessão de geração para um usuário
        
        Args:
            user_id: ID do usuário
            tipo_apartamento: Tipo do apartamento (essential, eco, bio, class)
            planta_bytes: Dados binários da planta
            comodos_data: Lista de cômodos detectados
            nome_planta: Nome da planta (opcional)
            ocr_texto: Textos extraídos via OCR
            interpretacao_llm: Análise do LLM
            
        Returns:
            tuple: (UserPlanta, ImageSession)
        """
        db = SessionLocal()
        try:
            # Criar a planta
            planta = create_user_planta(
                db=db,
                user_id=user_id,
                tipo_apartamento=tipo_apartamento,
                planta_data=planta_bytes,
                nome_planta=nome_planta,
                ocr_texto=ocr_texto,
                interpretacao=interpretacao_llm
            )
            
            # Atualizar contagem de cômodos
            planta.total_comodos_detectados = len(comodos_data)
            planta.status = "processando"
            db.commit()
            
            # Criar sessão de geração
            session = create_image_session(
                db=db,
                planta_id=planta.id,
                total_comodos=len(comodos_data)
            )
            
            return planta, session
            
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()
    
    @staticmethod
    def save_image(session_id: str, comodo_data: Dict[str, Any], 
                   image_data: bytes, prompt_usado: str,
                   tempo_geracao: float = None, tentativas: int = 1) -> Optional[GeneratedImage]:
        """
        Salva uma imagem gerada no banco de dados
        """
        db = SessionLocal()
        try:
            start_time = time.time()
            
            # Salvar imagem
            image_record = save_generated_image(
                db=db,
                session_id=session_id,
                comodo_data=comodo_data,
                imagem_data=image_data,
                prompt_usado=prompt_usado,
                tempo_geracao=tempo_geracao,
                tentativas=tentativas
            )
            
            # Atualizar progresso da sessão
            processing_time = time.time() - start_time
            update_session_progress(db, session_id, sucesso=True, tempo_geracao=processing_time)
            
            return image_record
            
        except Exception as e:
            db.rollback()
            logging.error(f"Erro ao salvar imagem no banco: {e}")
            
            # Atualizar progresso com erro
            update_session_progress(db, session_id, sucesso=False)
            return None
        finally:
            db.close()
    
    @staticmethod
    def get_user_plantas(user_id: int, limit: int = 50) -> List[UserPlanta]:
        """
        Recupera todas as plantas de um usuário
        """
        db = SessionLocal()
        try:
            return get_user_plantas(db, user_id, limit)
        finally:
            db.close()
    
    @staticmethod
    def get_planta_details(planta_id: int, user_id: int = None) -> Optional[UserPlanta]:
        """
        Recupera detalhes de uma planta específica
        """
        db = SessionLocal()
        try:
            query = db.query(UserPlanta).filter(UserPlanta.id == planta_id)
            if user_id:
                query = query.filter(UserPlanta.user_id == user_id)
            return query.first()
        finally:
            db.close()
    
    @staticmethod
    def get_planta_sessions(planta_id: int) -> List[ImageSession]:
        """
        Recupera todas as sessões de uma planta
        """
        db = SessionLocal()
        try:
            return get_planta_sessions(db, planta_id)
        finally:
            db.close()
    
    @staticmethod
    def get_session_images(session_id: str) -> List[GeneratedImage]:
        """
        Recupera todas as imagens de uma sessão
        """
        db = SessionLocal()
        try:
            return get_session_images(db, session_id)
        finally:
            db.close()
    
    @staticmethod
    def get_user_all_images(user_id: int, limit: int = 100) -> List[GeneratedImage]:
        """
        Recupera todas as imagens de um usuário
        """
        db = SessionLocal()
        try:
            return get_user_all_images(db, user_id, limit)
        finally:
            db.close()
    
    @staticmethod
    def get_image_data(image_id: int, user_id: int = None) -> Optional[bytes]:
        """
        Recupera os dados binários de uma imagem pelo ID
        """
        db = SessionLocal()
        try:
            query = db.query(GeneratedImage).filter(GeneratedImage.id == image_id)
            
            # Se user_id fornecido, verificar se a imagem pertence ao usuário
            if user_id:
                query = query.join(ImageSession).join(UserPlanta).filter(
                    UserPlanta.user_id == user_id
                )
            
            image = query.first()
            return image.imagem_data if image else None
        finally:
            db.close()
    
    @staticmethod
    def get_planta_data(planta_id: int, user_id: int = None) -> Optional[bytes]:
        """
        Recupera os dados binários de uma planta pelo ID
        """
        db = SessionLocal()
        try:
            query = db.query(UserPlanta).filter(UserPlanta.id == planta_id)
            if user_id:
                query = query.filter(UserPlanta.user_id == user_id)
                
            planta = query.first()
            return planta.planta_data if planta else None
        finally:
            db.close()
    
    @staticmethod
    def delete_planta(planta_id: int, user_id: int) -> bool:
        """
        Remove uma planta e todas suas sessões e imagens
        """
        db = SessionLocal()
        try:
            # Verificar se a planta pertence ao usuário
            planta = db.query(UserPlanta).filter(
                UserPlanta.id == planta_id,
                UserPlanta.user_id == user_id
            ).first()
            
            if not planta:
                return False
            
            # Remover a planta (cascade remove sessões e imagens)
            db.delete(planta)
            db.commit()
            return True
            
        except Exception as e:
            db.rollback()
            print(f"Erro ao deletar planta: {e}")
            return False
        finally:
            db.close()
    
    @staticmethod
    def get_user_stats(user_id: int) -> Dict[str, Any]:
        """
        Recupera estatísticas de um usuário
        """
        db = SessionLocal()
        try:
            # Contar plantas
            total_plantas = db.query(UserPlanta).filter(UserPlanta.user_id == user_id).count()
            
            # Contar sessões
            total_sessoes = db.query(ImageSession).join(UserPlanta).filter(
                UserPlanta.user_id == user_id
            ).count()
            
            # Contar imagens
            total_imagens = db.query(GeneratedImage).join(ImageSession).join(UserPlanta).filter(
                UserPlanta.user_id == user_id
            ).count()
            
            # Tamanho total das imagens
            total_size = db.query(db.func.sum(GeneratedImage.tamanho_bytes)).join(
                ImageSession
            ).join(UserPlanta).filter(UserPlanta.user_id == user_id).scalar() or 0
            
            # Estatísticas por tipo
            stats_by_type = db.query(
                UserPlanta.tipo_apartamento,
                db.func.count(UserPlanta.id).label('count')
            ).filter(UserPlanta.user_id == user_id).group_by(
                UserPlanta.tipo_apartamento
            ).all()
            
            return {
                "total_plantas": total_plantas,
                "total_sessoes": total_sessoes,
                "total_imagens": total_imagens,
                "total_size_bytes": total_size,
                "total_size_mb": round(total_size / (1024 * 1024), 2),
                "stats_by_type": [
                    {"tipo": stat[0], "plantas": stat[1]} 
                    for stat in stats_by_type
                ]
            }
        finally:
            db.close()


# Funções de conveniência para uso direto
def create_user_planta_session(user_id: int, tipo_apartamento: str, 
                              planta_bytes: bytes, comodos_data: List[Dict],
                              nome_planta: str = None, ocr_texto: str = None,
                              interpretacao_llm: str = None) -> tuple[UserPlanta, ImageSession]:
    """Função de conveniência para criar planta e sessão"""
    return ImageDatabaseService.create_planta_and_session(
        user_id, tipo_apartamento, planta_bytes, comodos_data,
        nome_planta, ocr_texto, interpretacao_llm
    )


def save_image_to_user_db(session_id: str, comodo_data: Dict[str, Any], 
                         image_data: bytes, prompt_usado: str,
                         tempo_geracao: float = None, tentativas: int = 1) -> Optional[GeneratedImage]:
    """Função de conveniência para salvar imagem"""
    return ImageDatabaseService.save_image(
        session_id, comodo_data, image_data, prompt_usado, tempo_geracao, tentativas
    )
