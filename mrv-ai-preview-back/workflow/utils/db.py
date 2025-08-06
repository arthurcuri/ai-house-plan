import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

logger = logging.getLogger(__name__)

# Configuração do banco de dados SQLite para desenvolvimento
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./auth.db")

# Engine configurado para SQLite com melhorias para desenvolvimento
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False},
    echo=False,  # Set True para ver SQL queries no log
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db() -> Session:
    """Dependency para obter sessão do banco de dados"""
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(f"Erro na sessão do banco de dados: {e}")
        db.rollback()
        raise
    finally:
        db.close()

def create_tables():
    """Criar todas as tabelas no banco de dados"""
    try:
        from auth.models import Base as AuthBase
        AuthBase.metadata.create_all(bind=engine)
        logger.info("Tabelas do SQLite criadas com sucesso")
    except Exception as e:
        logger.error(f"Erro ao criar tabelas: {e}")
        raise

def init_db():
    """Inicializar banco de dados SQLite"""
    create_tables()
    logger.info("Banco de dados SQLite inicializado para desenvolvimento")