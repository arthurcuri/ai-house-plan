#!/usr/bin/env python3
"""
Script para inicializar o banco de dados SQLite do MRV AI Preview
"""

import os
import sys
import logging
from pathlib import Path

# Adicionar utils ao path para imports
utils_path = Path(__file__).parent / "utils"
sys.path.insert(0, str(utils_path))

try:
    from database.db_service import init_db, SessionLocal
    from auth.models import User
    from auth.utils import hash_password
except ImportError as e:
    logging.error(f"Erro ao importar módulos: {e}")
    logging.error("Certifique-se de que todas as dependências estão instaladas")
    sys.exit(1)

def create_test_user():
    """Criar um usuário de teste para desenvolvimento"""
    db = SessionLocal()
    try:
        # Verificar se já existe um usuário de teste
        test_user = db.query(User).filter(User.email == "test@mrv.com").first()
        if test_user:
            return
        
        # Criar usuário de teste
        test_user = User(
            nome="Usuário Teste",
            email="test@mrv.com",
            senha_hashed=hash_password("123456")
        )
        db.add(test_user)
        db.commit()
    except Exception as e:
        logging.error(f"Erro ao criar usuário de teste: {e}")
        db.rollback()
    finally:
        db.close()

def main():
    """Função principal"""    
    try:
        # Inicializar banco de dados
        init_db()
        
        # Criar usuário de teste
        create_test_user()
        
        # Mostrar localização do banco
        db_path = os.path.abspath("./auth.db")
        
    except Exception as e:
        logging.error(f"Erro ao inicializar banco: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
