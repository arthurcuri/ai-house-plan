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
    print(f"Erro ao importar módulos: {e}")
    print("Certifique-se de que todas as dependências estão instaladas")
    sys.exit(1)

def create_test_user():
    """Criar um usuário de teste para desenvolvimento"""
    db = SessionLocal()
    try:
        # Verificar se já existe um usuário de teste
        test_user = db.query(User).filter(User.email == "test@mrv.com").first()
        if test_user:
            print("Usuário de teste já existe: test@mrv.com")
            return
        
        # Criar usuário de teste
        test_user = User(
            nome="Usuário Teste",
            email="test@mrv.com",
            senha_hashed=hash_password("123456")
        )
        db.add(test_user)
        db.commit()
        print("Usuário de teste criado: test@mrv.com / senha: 123456")
    except Exception as e:
        print(f"Erro ao criar usuário de teste: {e}")
        db.rollback()
    finally:
        db.close()

def main():
    """Função principal"""
    print("🏗️  Inicializando banco de dados SQLite para desenvolvimento...")
    
    try:
        # Inicializar banco de dados
        init_db()
        print("✅ Banco de dados SQLite inicializado com sucesso!")
        
        # Criar usuário de teste
        create_test_user()
        
        # Mostrar localização do banco
        db_path = os.path.abspath("./auth.db")
        print(f"📂 Banco de dados criado em: {db_path}")
        
        print("\n🚀 Sistema pronto para desenvolvimento!")
        print("📚 Acesse a documentação em: http://127.0.0.1:8000/docs")
        
    except Exception as e:
        print(f"❌ Erro ao inicializar banco: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
