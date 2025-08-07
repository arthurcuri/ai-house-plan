from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.exc import NoResultFound
from .utils import hash_password, verify_password

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    senha_hashed = Column(String(255), nullable=False)

# Funções utilitárias para autenticação

def get_user_by_email(session: Session, email: str):
    try:
        return session.query(User).filter(User.email == email).one()
    except NoResultFound:
        return None

def authenticate_user(session: Session, email: str, senha: str):
    user = get_user_by_email(session, email)
    if user and verify_password(senha, user.senha_hashed):
        return user
    return None