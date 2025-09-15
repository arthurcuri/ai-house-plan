#!/usr/bin/env python3
"""
MRV AI Preview - Aplicação Principal
Sistema organizado para análise de plantas arquitetônicas e geração de imagens 3D.
"""

# Executar a aplicação FastAPI
if __name__ == "__main__":
    import uvicorn
    import sys
    from pathlib import Path
    
    # Adicionar utils ao path para imports
    utils_path = Path(__file__).parent / "utils"
    sys.path.insert(0, str(utils_path))
    
    from utils.api.main import app
    
    # Configurar CORS para permitir conexões do frontend
    from fastapi.middleware.cors import CORSMiddleware
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    uvicorn.run(
        "utils.api.main:app",
        host="127.0.0.1",
        port=8000,
        log_level="info",
        reload=True,  # Auto-reload durante desenvolvimento
        access_log=True  # Log de acesso para debug
    )
