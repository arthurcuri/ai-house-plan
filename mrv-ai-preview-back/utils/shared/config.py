import os
from typing import List

class Settings:
    # JWT Settings
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "dev-secret-key-change-in-production")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
    
    # Database Settings - SQLite para desenvolvimento
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./auth.db")
    
    # CORS Settings para desenvolvimento
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:3001",  # Para outros ports de dev
    ]
    
    # Environment
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"
    
    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "MRV AI Preview API - Development"
    
    # Security - configurações mais relaxadas para desenvolvimento
    BCRYPT_ROUNDS: int = 4  # Mais rápido para desenvolvimento
    
    # Rate Limiting - mais permissivo em desenvolvimento
    RATE_LIMIT_PER_MINUTE: int = int(os.getenv("RATE_LIMIT_PER_MINUTE", "120"))
    
    # SQLite specific settings
    SQLITE_ECHO: bool = os.getenv("SQLITE_ECHO", "false").lower() == "true"

settings = Settings()
