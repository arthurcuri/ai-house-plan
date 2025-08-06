#!/usr/bin/env python3

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Carregar variáveis do .env
load_dotenv()

# Verificar se a API key está configurada
api_key = os.getenv("GEMINI_API_KEY_LUCAS")
print(f"API Key configurada: {'Sim' if api_key else 'Não'}")
print(f"Tamanho da API Key: {len(api_key) if api_key else 0}")

if api_key:
    try:
        genai.configure(api_key=api_key)
        modelo = genai.GenerativeModel("gemini-1.5-flash")
        
        # Teste simples
        response = modelo.generate_content("Diga apenas 'OK' se você conseguir me ouvir")
        print(f"Resposta do Gemini: {response.text}")
        print("✅ API do Gemini funcionando corretamente!")
        
    except Exception as e:
        print(f"❌ Erro ao testar API do Gemini: {e}")
else:
    print("❌ API Key do Gemini não encontrada no arquivo .env")
    print("Certifique-se de que existe um arquivo .env com a variável GEMINI_API_KEY_LUCAS")
