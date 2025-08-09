from dotenv import load_dotenv
import os
import google.generativeai as genai

def test_gemini_api():
    # Carrega as variáveis de ambiente
    load_dotenv()
    
    # Obtém a chave API
    api_key = os.getenv("GEMINI_API_KEY_LUCAS")
    print(f"Testando com a chave API: {api_key[:10]}...")
    
    try:
        # Configura o cliente
        genai.configure(api_key=api_key)
        
        # Cria uma instância do modelo
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Tenta uma chamada simples
        response = model.generate_content("Olá, isso é um teste da API.")
        
        print("\n✅ API funcionando corretamente!")
        print("Resposta do modelo:", response.text)
        
    except Exception as e:
        print("\n❌ Erro ao testar a API:")
        print(str(e))

if __name__ == "__main__":
    test_gemini_api()
