from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

# Configuração do banco de dados SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./auth.db"

# Para PostgreSQL, use algo como:
# SQLALCHEMY_DATABASE_URL = "postgresql://usuario:senha@localhost/nome_do_banco"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False} if "sqlite" in SQLALCHEMY_DATABASE_URL else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Dependency para obter sessão do banco de dados"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    """Criar todas as tabelas no banco de dados"""
    from .auth.models import Base as AuthBase
    AuthBase.metadata.create_all(bind=engine)