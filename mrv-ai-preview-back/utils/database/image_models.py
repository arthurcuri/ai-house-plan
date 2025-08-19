"""
Modelos de dados para armazenamento de imagens no banco SQLite
Estrutura hierárquica: Usuário → Plantas → Sessões → Cômodos → Imagens
"""

from sqlalchemy import Column, Integer, String, Text, DateTime, BLOB, Float, Boolean, ForeignKey
from sqlalchemy.orm import Session, relationship
from datetime import datetime

# Importar Base do módulo principal
from .db_service import Base


class UserPlanta(Base):
    """
    Modelo para armazenar plantas baixas enviadas pelos usuários
    Um usuário pode ter várias plantas
    """
    __tablename__ = "user_plantas"
    
    # Identificação
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    
    # Informações da planta
    nome_planta = Column(String(200))  # Nome dado pelo usuário
    tipo_apartamento = Column(String(50), nullable=False)  # essential, eco, bio, class
    
    # Hash para identificar plantas duplicadas
    planta_hash = Column(String(64), index=True)  # MD5 da imagem original
    
    # Dados da planta original
    planta_data = Column(BLOB)  # Dados binários da planta original
    tamanho_bytes = Column(Integer)
    formato_original = Column(String(10))  # JPG, PNG, etc.
    
    # Análise da planta
    total_comodos_detectados = Column(Integer, default=0)
    ocr_texto_extraido = Column(Text)  # Textos extraídos via OCR
    interpretacao_llm = Column(Text)  # Análise do LLM
    
    # Metadados
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Status da planta
    status = Column(String(50), default="processando")  # processando, concluida, erro
    
    # Relacionamentos
    # user = relationship("User", back_populates="plantas")
    sessoes = relationship("ImageSession", back_populates="planta", cascade="all, delete-orphan")


class ImageSession(Base):
    """
    Modelo para gerenciar sessões de geração de imagens
    Uma planta pode ter várias sessões (regenerações)
    """
    __tablename__ = "image_sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(100), unique=True, index=True, nullable=False)
    
    # Relacionamento com planta
    planta_id = Column(Integer, ForeignKey("user_plantas.id"), nullable=False, index=True)
    
    # Informações da sessão
    total_comodos = Column(Integer, nullable=False)
    comodos_processados = Column(Integer, default=0)
    comodos_sucesso = Column(Integer, default=0)
    comodos_erro = Column(Integer, default=0)
    
    # Status da sessão
    status = Column(String(50), default="em_progresso")  # em_progresso, concluida, erro, cancelada
    
    # Configurações usadas
    alta_qualidade = Column(Boolean, default=True)
    max_tentativas = Column(Integer, default=8)
    
    # Metadados
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    tempo_processamento = Column(Float)  # Tempo em segundos
    
    # Relacionamentos
    planta = relationship("UserPlanta", back_populates="sessoes")
    imagens = relationship("GeneratedImage", back_populates="sessao", cascade="all, delete-orphan")


class GeneratedImage(Base):
    """
    Modelo para armazenar imagens geradas pelo sistema
    Uma sessão pode ter várias imagens (uma por cômodo)
    """
    __tablename__ = "generated_images"
    
    # Identificação
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(100), ForeignKey("image_sessions.session_id"), nullable=False, index=True)
    comodo_id = Column(Integer, nullable=False)  # Número do cômodo (1, 2, 3, etc.)
    
    # Informações do cômodo
    nome_comodo = Column(String(200), nullable=False)  # Nome original do cômodo
    nome_arquivo = Column(String(255), nullable=False)  # Nome sanitizado do arquivo
    tipo_comodo = Column(String(100))  # Tipo classificado (quarto_casal, sala, etc.)
    
    # Dimensões do cômodo (em cm)
    largura_cm = Column(Float)
    comprimento_cm = Column(Float)
    localizacao = Column(String(200))  # Localização na planta
    
    # Dados da imagem
    imagem_data = Column(BLOB, nullable=False)  # Dados binários da imagem
    tamanho_bytes = Column(Integer, nullable=False)
    formato = Column(String(10), default="PNG")  # Formato da imagem
    resolucao = Column(String(20), default="MAX_QUALITY")  # Resolução máxima
    
    # Configurações de geração
    prompt_usado = Column(Text)  # Prompt completo usado para gerar a imagem
    alta_qualidade = Column(Boolean, default=True)
    qualidade_jpeg = Column(Integer, default=100)  # Qualidade de compressão JPEG
    
    # Performance da geração
    tempo_geracao = Column(Float)  # Tempo em segundos para gerar
    tentativas_realizadas = Column(Integer, default=1)  # Quantas tentativas foram necessárias
    
    # Metadados
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # URLs e paths (para compatibilidade)
    url_relativa = Column(String(500))  # URL relativa para acesso via web
    arquivo_path = Column(String(1000))  # Path completo do arquivo no sistema
    
    # Relacionamentos
    sessao = relationship("ImageSession", back_populates="imagens")


# Funções utilitárias para manipulação de imagens e plantas

def create_user_planta(db: Session, user_id: int, tipo_apartamento: str, 
                      planta_data: bytes, nome_planta: str = None, 
                      ocr_texto: str = None, interpretacao: str = None) -> UserPlanta:
    """
    Cria uma nova planta para um usuário
    """
    import hashlib
    
    # Gerar hash da planta
    planta_hash = hashlib.md5(planta_data).hexdigest()
    
    # Verificar se já existe planta igual para o usuário
    existing = db.query(UserPlanta).filter(
        UserPlanta.user_id == user_id,
        UserPlanta.planta_hash == planta_hash
    ).first()
    
    if existing:
        return existing
    
    planta = UserPlanta(
        user_id=user_id,
        nome_planta=nome_planta or f"Planta {datetime.now().strftime('%Y%m%d_%H%M%S')}",
        tipo_apartamento=tipo_apartamento,
        planta_hash=planta_hash,
        planta_data=planta_data,
        tamanho_bytes=len(planta_data),
        ocr_texto_extraido=ocr_texto,
        interpretacao_llm=interpretacao
    )
    db.add(planta)
    db.commit()
    db.refresh(planta)
    return planta


def create_image_session(db: Session, planta_id: int, total_comodos: int) -> ImageSession:
    """
    Cria uma nova sessão de geração de imagens para uma planta
    """
    import uuid
    from datetime import datetime
    
    # Gerar ID único da sessão
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_uuid = str(uuid.uuid4())[:8]
    session_id = f"{timestamp}_{session_uuid}"
    
    session = ImageSession(
        session_id=session_id,
        planta_id=planta_id,
        total_comodos=total_comodos
    )
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


def save_generated_image(db: Session, session_id: str, comodo_data: dict, 
                        imagem_data: bytes, prompt_usado: str, 
                        tempo_geracao: float = None, tentativas: int = 1) -> GeneratedImage:
    """
    Salva uma imagem gerada no banco de dados
    """
    # Sanitizar nome do arquivo
    nome_arquivo = _sanitizar_nome_arquivo(comodo_data.get('nome', 'comodo'))
    
    # Extrair dimensões se disponíveis
    dimensoes = comodo_data.get('dimensões', {}) or comodo_data.get('dimensoes', {})
    largura = dimensoes.get('largura') if dimensoes else None
    comprimento = dimensoes.get('comprimento') if dimensoes else None
    
    image_record = GeneratedImage(
        session_id=session_id,
        comodo_id=comodo_data.get('id', 0),
        nome_comodo=comodo_data.get('nome', 'Cômodo'),
        nome_arquivo=nome_arquivo,
        tipo_comodo=comodo_data.get('tipo'),
        largura_cm=largura,
        comprimento_cm=comprimento,
        localizacao=comodo_data.get('localização') or comodo_data.get('localizacao'),
        imagem_data=imagem_data,
        tamanho_bytes=len(imagem_data),
        prompt_usado=prompt_usado,
        alta_qualidade=comodo_data.get('alta_qualidade', True),
        tempo_geracao=tempo_geracao,
        tentativas_realizadas=tentativas,
        url_relativa=f"/database/images/{session_id}/{nome_arquivo}",
        arquivo_path=comodo_data.get('arquivo')
    )
    
    db.add(image_record)
    db.commit()
    db.refresh(image_record)
    return image_record


def get_user_plantas(db: Session, user_id: int, limit: int = 50) -> list[UserPlanta]:
    """
    Recupera todas as plantas de um usuário
    """
    return db.query(UserPlanta).filter(
        UserPlanta.user_id == user_id
    ).order_by(UserPlanta.created_at.desc()).limit(limit).all()


def get_planta_sessions(db: Session, planta_id: int) -> list[ImageSession]:
    """
    Recupera todas as sessões de uma planta
    """
    return db.query(ImageSession).filter(
        ImageSession.planta_id == planta_id
    ).order_by(ImageSession.created_at.desc()).all()


def get_session_images(db: Session, session_id: str) -> list[GeneratedImage]:
    """
    Recupera todas as imagens de uma sessão
    """
    return db.query(GeneratedImage).filter(
        GeneratedImage.session_id == session_id
    ).order_by(GeneratedImage.comodo_id).all()


def get_user_all_images(db: Session, user_id: int, limit: int = 100) -> list[GeneratedImage]:
    """
    Recupera todas as imagens de um usuário (de todas as plantas e sessões)
    """
    return db.query(GeneratedImage).join(
        ImageSession, GeneratedImage.session_id == ImageSession.session_id
    ).join(
        UserPlanta, ImageSession.planta_id == UserPlanta.id
    ).filter(
        UserPlanta.user_id == user_id
    ).order_by(GeneratedImage.created_at.desc()).limit(limit).all()


def update_session_progress(db: Session, session_id: str, sucesso: bool, 
                           tempo_geracao: float = None):
    """
    Atualiza o progresso de uma sessão de geração
    """
    session = db.query(ImageSession).filter(ImageSession.session_id == session_id).first()
    if session:
        session.comodos_processados += 1
        if sucesso:
            session.comodos_sucesso += 1
        else:
            session.comodos_erro += 1
        
        # Atualizar tempo de processamento
        if tempo_geracao:
            session.tempo_processamento = (session.tempo_processamento or 0) + tempo_geracao
        
        # Verificar se terminou
        if session.comodos_processados >= session.total_comodos:
            if session.comodos_erro == 0:
                session.status = "concluida"
            elif session.comodos_sucesso > 0:
                session.status = "concluida_com_erros"
            else:
                session.status = "erro"
        
        session.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(session)
    return session


def _sanitizar_nome_arquivo(nome: str) -> str:
    """
    Sanitiza nome de arquivo removendo caracteres problemáticos
    """
    import re
    
    nome_limpo = nome.replace('/', '_')
    nome_limpo = nome_limpo.replace('\\', '_')
    nome_limpo = nome_limpo.replace(' ', '_')
    nome_limpo = nome_limpo.replace(':', '_')
    nome_limpo = nome_limpo.replace('?', '_')
    nome_limpo = nome_limpo.replace('*', '_')
    nome_limpo = nome_limpo.replace('<', '_')
    nome_limpo = nome_limpo.replace('>', '_')
    nome_limpo = nome_limpo.replace('|', '_')
    nome_limpo = nome_limpo.replace('"', '_')
    
    nome_limpo = re.sub(r'_+', '_', nome_limpo)
    nome_limpo = nome_limpo.strip('_')
    nome_limpo = nome_limpo.lower()
    
    if not nome_limpo:
        nome_limpo = "comodo_sem_nome"
    
    return nome_limpo
