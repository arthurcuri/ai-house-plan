#!/usr/bin/env python3

import sys
import os

# Adicionar o diretório atual ao path
sys.path.insert(0, os.getcwd())

print("🔍 Testando importações...")

try:
    from llm_factory import interpretar_planta_com_imagem, gerar_imagem
    print("✅ llm_factory importado com sucesso")
    
    # Verificar se as funções existem
    print(f"✅ interpretar_planta_com_imagem: {callable(interpretar_planta_com_imagem)}")
    print(f"✅ gerar_imagem: {callable(gerar_imagem)}")
    
except Exception as e:
    print(f"❌ Erro ao importar llm_factory: {e}")
    
try:
    from interpreter_plan import interpretar_planta_com_ocr
    print("✅ interpreter_plan importado com sucesso")
except Exception as e:
    print(f"❌ Erro ao importar interpreter_plan: {e}")

try:
    from ocr_reader import reader
    print("✅ ocr_reader importado com sucesso")
except Exception as e:
    print(f"❌ Erro ao importar ocr_reader: {e}")

try:
    from pipeline_generate_images import gerar_imagens_para_comodos
    print("✅ pipeline_generate_images importado com sucesso")
except Exception as e:
    print(f"❌ Erro ao importar pipeline_generate_images: {e}")

try:
    from json_utils import limpar_json_llm
    print("✅ json_utils importado com sucesso")
except Exception as e:
    print(f"❌ Erro ao importar json_utils: {e}")

print("\n🧪 Teste de API Gemini...")
try:
    from dotenv import load_dotenv
    import google.generativeai as genai
    
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY_LUCAS")
    
    if api_key and api_key != "your_gemini_api_key_here":
        genai.configure(api_key=api_key)
        modelo = genai.GenerativeModel("gemini-1.5-flash")
        
        response = modelo.generate_content("Responda apenas 'OK' se conseguir me ouvir")
        print(f"✅ Resposta do Gemini: {response.text.strip()}")
    else:
        print("⚠️ API Key do Gemini não configurada corretamente")
        
except Exception as e:
    print(f"❌ Erro no teste do Gemini: {e}")

print("\n✅ Teste concluído!")
