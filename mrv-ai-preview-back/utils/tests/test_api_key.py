#!/usr/bin/env python3
"""
Script para testar a chave API do Google Gemini
Verifica se a chave está configurada, é válida e tem acesso aos modelos pagos
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Adicionar utils ao path
backend_path = Path(__file__).parent
sys.path.insert(0, str(backend_path))

# Carregar variáveis de ambiente
load_dotenv()

def test_env_config():
    """Testa se a chave está configurada no .env"""
    print("=" * 60)
    print("TESTE 1: Verificando configuração do .env")
    print("=" * 60)
    
    api_key = os.getenv("GEMINI_API_KEY_LUCAS")
    
    if not api_key:
        print("❌ ERRO: GEMINI_API_KEY_LUCAS não encontrada no .env")
        print("\nCertifique-se de ter o arquivo .env com:")
        print("GEMINI_API_KEY_LUCAS=sua_chave_aqui")
        return False
    
    # Mostrar parte da chave (segurança)
    masked_key = f"{api_key[:10]}...{api_key[-4:]}" if len(api_key) > 14 else "***"
    print(f"✅ Chave encontrada: {masked_key}")
    print(f"   Comprimento: {len(api_key)} caracteres")
    return True, api_key

def test_basic_import():
    """Testa se as bibliotecas estão instaladas"""
    print("\n" + "=" * 60)
    print("TESTE 2: Verificando bibliotecas instaladas")
    print("=" * 60)
    
    try:
        import google.generativeai as genai
        print("✅ google.generativeai importado com sucesso")
    except ImportError as e:
        print(f"❌ ERRO ao importar google.generativeai: {e}")
        return False
    
    try:
        from google import genai as genai_new
        print("✅ google.genai (nova API) importado com sucesso")
        return True, genai, genai_new
    except ImportError as e:
        print(f"⚠️  AVISO: google.genai não disponível: {e}")
        print("   Isso é normal se não tiver a versão mais recente")
        return True, genai, None

def test_api_key_validity(genai, api_key):
    """Testa se a chave API é válida"""
    print("\n" + "=" * 60)
    print("TESTE 3: Verificando validade da chave API")
    print("=" * 60)
    
    try:
        genai.configure(api_key=api_key)
        
        # Tentar listar modelos disponíveis
        print("Tentando listar modelos disponíveis...")
        models = list(genai.list_models())
        
        if not models:
            print("⚠️  AVISO: Nenhum modelo encontrado")
            return False
        
        print(f"✅ Chave API válida! {len(models)} modelos encontrados")
        
        # Mostrar alguns modelos disponíveis
        print("\nModelos disponíveis (primeiros 10):")
        for i, model in enumerate(models[:10], 1):
            print(f"   {i}. {model.name}")
        
        return True, models
    except Exception as e:
        error_msg = str(e)
        if "API_KEY" in error_msg or "401" in error_msg or "403" in error_msg:
            print(f"❌ ERRO: Chave API inválida ou sem permissões")
            print(f"   Detalhes: {error_msg[:200]}")
        else:
            print(f"❌ ERRO ao verificar chave: {error_msg[:200]}")
        return False

def test_text_model(genai, api_key):
    """Testa o modelo de texto"""
    print("\n" + "=" * 60)
    print("TESTE 4: Testando modelo de texto (gemini-2.5-flash)")
    print("=" * 60)
    
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        print("✅ Modelo carregado com sucesso")
        
        print("Enviando requisição de teste...")
        response = model.generate_content("Responda apenas: OK")
        print(f"✅ Resposta recebida: {response.text.strip()}")
        return True
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "quota" in error_msg.lower():
            print(f"⚠️  AVISO: Quota excedida ou limite atingido")
            print(f"   Isso pode indicar que ainda está no free tier")
            print(f"   Erro: {error_msg[:200]}")
        else:
            print(f"❌ ERRO: {error_msg[:200]}")
        return False

def test_image_model(genai_new, api_key):
    """Testa o modelo de geração de imagens"""
    print("\n" + "=" * 60)
    print("TESTE 5: Testando modelo de imagens (gemini-2.5-flash-image)")
    print("=" * 60)
    
    if not genai_new:
        print("⚠️  AVISO: google.genai não disponível, pulando teste de imagens")
        return None
    
    try:
        from google.genai import types
        client = genai_new.Client(api_key=api_key)
        
        print("Enviando requisição de teste de geração de imagem...")
        response = client.models.generate_content(
            model="gemini-2.5-flash-image",
            contents="Create a simple red circle on white background",
            config=types.GenerateContentConfig(
                response_modalities=['IMAGE'],
                max_output_tokens=1024,
            )
        )
        
        # Verificar se recebeu imagem
        image_received = False
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                image_received = True
                print(f"✅ Imagem gerada com sucesso! Tamanho: {len(part.inline_data.data)} bytes")
                break
        
        if not image_received:
            print("⚠️  AVISO: Resposta recebida mas nenhuma imagem encontrada")
        
        return image_received
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "quota" in error_msg.lower():
            print(f"⚠️  AVISO: Quota excedida ou modelo não disponível no seu plano")
            print(f"   Erro: {error_msg[:200]}")
        elif "not found" in error_msg.lower() or "404" in error_msg:
            print(f"⚠️  AVISO: Modelo não encontrado ou não disponível")
            print(f"   Verifique se tem acesso ao plano pago")
        else:
            print(f"❌ ERRO: {error_msg[:200]}")
        return False

def test_multimodal_model(genai, api_key):
    """Testa o modelo multimodal"""
    print("\n" + "=" * 60)
    print("TESTE 6: Testando modelo multimodal")
    print("=" * 60)
    
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        
        # Criar uma imagem simples de teste
        from PIL import Image
        import io
        
        # Criar imagem de teste (100x100 pixels, cor azul)
        test_image = Image.new('RGB', (100, 100), color='blue')
        img_bytes = io.BytesIO()
        test_image.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        
        print("Enviando requisição multimodal (texto + imagem)...")
        response = model.generate_content([
            {"mime_type": "image/png", "data": img_bytes.getvalue()},
            {"text": "What color is this image? Answer in one word."}
        ])
        
        print(f"✅ Resposta recebida: {response.text.strip()}")
        return True
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "quota" in error_msg.lower():
            print(f"⚠️  AVISO: Quota excedida")
            print(f"   Erro: {error_msg[:200]}")
        else:
            print(f"❌ ERRO: {error_msg[:200]}")
        return False

def main():
    """Função principal"""
    print("\n" + "=" * 60)
    print("TESTE DE CHAVE API - Google Gemini")
    print("=" * 60)
    
    results = {}
    
    # Teste 1: Configuração
    env_result = test_env_config()
    if not env_result:
        print("\n❌ Testes interrompidos: chave não configurada")
        return
    _, api_key = env_result if isinstance(env_result, tuple) else (False, None)
    
    # Teste 2: Imports
    import_result = test_basic_import()
    if not import_result:
        print("\n❌ Testes interrompidos: bibliotecas não disponíveis")
        return
    genai, genai_new = import_result[1], import_result[2] if len(import_result) > 2 else None
    
    # Teste 3: Validade da chave
    validity_result = test_api_key_validity(genai, api_key)
    if not validity_result:
        print("\n❌ Testes interrompidos: chave inválida")
        return
    models = validity_result[1] if isinstance(validity_result, tuple) else None
    
    # Teste 4: Modelo de texto
    results['texto'] = test_text_model(genai, api_key)
    
    # Teste 5: Modelo de imagens
    results['imagem'] = test_image_model(genai_new, api_key)
    
    # Teste 6: Modelo multimodal
    results['multimodal'] = test_multimodal_model(genai, api_key)
    
    # Resumo final
    print("\n" + "=" * 60)
    print("RESUMO DOS TESTES")
    print("=" * 60)
    
    print(f"✅ Configuração: OK")
    print(f"✅ Bibliotecas: OK")
    print(f"✅ Chave API: Válida")
    print(f"{'✅' if results.get('texto') else '❌'} Modelo de Texto: {'OK' if results.get('texto') else 'FALHOU'}")
    print(f"{'✅' if results.get('imagem') else '⚠️ '} Modelo de Imagens: {'OK' if results.get('imagem') else 'NÃO TESTADO/FALHOU'}")
    print(f"{'✅' if results.get('multimodal') else '❌'} Modelo Multimodal: {'OK' if results.get('multimodal') else 'FALHOU'}")
    
    # Verificar se tem acesso a modelos pagos
    if models:
        paid_models = [m.name for m in models if "pro" in m.name.lower() or "image" in m.name.lower()]
        if paid_models:
            print(f"\n✅ Modelos pagos disponíveis: {len(paid_models)}")
            print("   Primeiros modelos:")
            for model in paid_models[:5]:
                print(f"   - {model}")
        else:
            print("\n⚠️  AVISO: Nenhum modelo pago detectado")
            print("   Isso pode indicar que ainda está no free tier")
    
    print("\n" + "=" * 60)
    print("Testes concluídos!")
    print("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nTeste interrompido pelo usuário")
    except Exception as e:
        print(f"\n\n❌ ERRO FATAL: {e}")
        import traceback
        traceback.print_exc()