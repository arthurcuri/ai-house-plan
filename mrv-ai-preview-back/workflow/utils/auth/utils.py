import hashlib
import secrets
from jose import jwt, JWTError
from datetime import datetime, timedelta

# Configurações JWT
SECRET_KEY = "sua_chave_secreta_supersegura"  # Troque por uma chave forte em produção
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def hash_password(password: str) -> str:
    """Hash da senha usando SHA-256 com salt"""
    # Gerar um salt aleatório
    salt = secrets.token_hex(32)
    # Combinar senha com salt e fazer hash
    pwd_hash = hashlib.sha256((password + salt).encode()).hexdigest()
    # Retornar salt + hash concatenados
    return f"{salt}${pwd_hash}"

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verificar senha comparando com hash armazenado"""
    try:
        # Separar salt e hash
        salt, stored_hash = hashed_password.split('$')
        # Hash da senha fornecida com o mesmo salt
        pwd_hash = hashlib.sha256((plain_password + salt).encode()).hexdigest()
        # Comparar hashes
        return pwd_hash == stored_hash
    except ValueError:
        return False

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None