#!/usr/bin/env python3
"""
Script para inicializar o banco de dados SQLite do MRV AI Preview
"""

import os
import sys
import logging
from pathlib import Path

# Adicionar o diretório do backend ao path (não apenas utils)
backend_path = Path(__file__).parent
sys.path.insert(0, str(backend_path))

# Agora podemos importar usando o caminho completo
try:
    from utils.database.db_service import init_db, SessionLocal, engine, Base
    from utils.auth.models import User
    from utils.auth.utils import hash_password
    from utils.database.architect_models import (
    ArchitectPersonalType,
    TypeReferencePhoto,
    TypeRoomPrompt
)
except ImportError as e:
    logging.error(f"Erro ao importar módulos: {e}")
    logging.error("Certifique-se de que todas as dependências estão instaladas")
    import traceback
    traceback.print_exc()
    sys.exit(1)

def create_test_user():
    """Criar um usuário de teste para desenvolvimento"""
    db = SessionLocal()
    try:
        # Verificar se já existe um usuário de teste
        test_user = db.query(User).filter(User.email == "test@mrv.com").first()
        if test_user:
            logging.info("Usuário de teste já existe")
            return
        
        # Criar usuário de teste
        test_user = User(
            nome="Usuário Teste",
            email="test@mrv.com",
            senha_hashed=hash_password("123456")
        )
        db.add(test_user)
        db.commit()
        logging.info("Usuário de teste criado com sucesso")
    except Exception as e:
        logging.error(f"Erro ao criar usuário de teste: {e}")
        db.rollback()
        import traceback
        traceback.print_exc()
    finally:
        db.close()

def main():
    """Função principal"""
    logging.basicConfig(level=logging.INFO)
    
    try:
        # Criar TODAS as tabelas usando Base.metadata.create_all()
        # Isso garante que todas as foreign keys sejam resolvidas corretamente
        Base.metadata.create_all(bind=engine)
        logging.info("Todas as tabelas criadas com sucesso")
        
        # Criar usuário de teste
        create_test_user()
        
        # Mostrar localização do banco
        db_path = os.path.abspath("./auth.db")
        logging.info(f"Banco de dados inicializado em: {db_path}")
        
    except Exception as e:
        logging.error(f"Erro ao inicializar banco: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

        
if __name__ == "__main__":
    main()