import uvicorn

if __name__ == "__main__":
    print("🚀 Iniciando servidor FastAPI na porta 8000...")
    print("📡 Rota disponível: http://127.0.0.1:8000/ocr")
    print("📚 Documentação: http://127.0.0.1:8000/docs")
    
    uvicorn.run(
        "ocr_plan:app",  # Import string format para funcionar com reload
        host="127.0.0.1", 
        port=8000, 
        reload=True,
        log_level="info"
    ) 