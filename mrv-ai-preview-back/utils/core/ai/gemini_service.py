import google.generativeai as genai
from dotenv import load_dotenv
import os
from PIL import Image
from io import BytesIO
import base64
import time
import random
import warnings

# Suprimir warnings desnecessários do PyTorch
warnings.filterwarnings("ignore", category=UserWarning, module="torch")
warnings.filterwarnings("ignore", message=".*pin_memory.*")

# Tentar importar a nova API do Gemini
try:
    from google import genai as genai_new
    from google.genai import types
    GEMINI_2_AVAILABLE = True
except ImportError:
    GEMINI_2_AVAILABLE = False

# Lógica usando GEMINI
# Carregar variáveis do .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY_LUCAS")
genai.configure(api_key=GEMINI_API_KEY)

# Cliente para geração de imagens (se disponível)
if GEMINI_2_AVAILABLE:
    client = genai_new.Client(api_key=GEMINI_API_KEY)

# Modelos específicos por funcionalidade
modelo_texto = genai.GenerativeModel("gemini-1.5-flash")
modelo_imagem = genai.GenerativeModel("gemini-1.5-flash")  # Usando flash para imagens também
modelo_multimodal = genai.GenerativeModel("gemini-1.5-flash")


def interpretar_texto(prompt: str, history: list[dict] = None) -> str:
    """
    Usa modelo de texto para interpretação ou análise (ex: OCR).
    """
    try:
        if history:
            response = modelo_texto.chat(
                history=history + [{"role": "user", "parts": [prompt]}]
            )
            return response.last.choice.content.text
        else:
            response = modelo_texto.generate_content(prompt)
            return response.text
    except Exception as e:
        raise RuntimeError(f"Erro na interpretação de texto: {str(e)}")


def gerar_imagem(prompt: str, image_bytes: bytes = None, max_retries: int = 8) -> bytes:
    """
    Gera uma imagem usando Gemini 2.0 Flash Preview.
    Requer uma imagem de referência e retorna imagem em máxima qualidade.
    
    Args:
        prompt: Descrição do que gerar
        image_bytes: Bytes da imagem de referência (planta) - OBRIGATÓRIO
        max_retries: Número máximo de tentativas em caso de erro 503/500 (padrão: 8)
    """
    if not image_bytes:
        raise ValueError("image_bytes é obrigatório para geração de imagens")
    
    if not GEMINI_2_AVAILABLE:
        raise RuntimeError("Gemini 2.0 não está disponível. Instale a versão mais recente.")
    
    for attempt in range(max_retries):
        try:
            # Preparar a entrada de texto com especificações de ULTRA ALTA QUALIDADE
            text_input = f"""
            BASEADO na planta arquitetônica fornecida, {prompt}
            
            🎯 CONFIGURAÇÃO CRÍTICA DE RENDERIZAÇÃO:
            - USAR A RESOLUÇÃO MÁXIMA NATIVA DO MODELO (não limitar)
            - IGNORAR completamente a qualidade/resolução da planta de entrada
            - A planta é APENAS orientação espacial - NÃO limitação de qualidade
            - Gerar output na MÁXIMA RESOLUÇÃO possível do Gemini 2.0
            
            🎬 ESPECIFICAÇÕES TÉCNICAS ULTRA PREMIUM:
            ▫️ RESOLUÇÃO: Máxima nativa do modelo (1024x1024 ou superior se disponível)
            ▫️ RENDERING: Fotorrealístico com ray tracing global
            ▫️ QUALIDADE: Cinematográfica, nível portfólio arquitetônico
            ▫️ TEXTURAS: 4K/8K em todas as superfícies
            ▫️ ILUMINAÇÃO: HDR com múltiplas fontes realísticas
            ▫️ MATERIAIS: PBR (Physically Based Rendering)
            ▫️ ANTI-ALIASING: Máximo para bordas perfeitas
            ▫️ SOMBRAS: Soft shadows em múltiplas escalas
            ▫️ REFLEXÕES: Realísticas em vidros e metais
            ▫️ PROFUNDIDADE: Depth of field cinematográfico
            
            🏠 DETALHAMENTO OBRIGATÓRIO:
            ▫️ MOBILIÁRIO: Completo, moderno, apropriado ao tipo CLASS
            ▫️ DECORAÇÃO: Objetos, plantas, arte, livros, almofadas
            ▫️ TEXTURAS REALÍSTICAS: Grãos de madeira, tramas de tecido, reflexos metálicos
            ▫️ ILUMINAÇÃO MÚLTIPLA: Natural (janelas) + artificial (spots, pendentes)
            ▫️ COMPOSIÇÃO: Perspectiva arquitetônica profissional
            ▫️ ACABAMENTOS: Premium, detalhados, fotorrealísticos
            
            ⚡ COMANDO FINAL:
            MESMO que a planta seja simples/pixelizada, você DEVE criar um ambiente 
            LUXUOSO, COMPLETO e FOTORREALÍSTICO em MÁXIMA RESOLUÇÃO.
            A imagem deve ser indistinguível de uma fotografia profissional 4K.
            """
            
            # Converter bytes para PIL Image mantendo máxima qualidade
            reference_image = Image.open(BytesIO(image_bytes))
            
            # CRITICAL: A imagem é apenas REFERÊNCIA - não afeta qualidade final do output
            # Se muito pequena, aplicar upscaling mínimo apenas para compatibilidade
            min_size = 512  # Tamanho mínimo apenas para compatibilidade da API
            if reference_image.size[0] < min_size or reference_image.size[1] < min_size:
                scale_factor = max(min_size / reference_image.size[0], min_size / reference_image.size[1])
                new_size = (int(reference_image.size[0] * scale_factor), int(reference_image.size[1] * scale_factor))
                reference_image = reference_image.resize(new_size, Image.Resampling.LANCZOS)
            
            # Garantir que está no formato RGB para compatibilidade
            if reference_image.mode != 'RGB':
                reference_image = reference_image.convert('RGB')
            
            # Preparar conteúdo com imagem de referência
            contents = [text_input, reference_image]
            
            # Gerar conteúdo com o modelo de geração de imagens em MÁXIMA QUALIDADE NATIVA
            response = client.models.generate_content(
                model="gemini-2.0-flash-preview-image-generation",
                contents=contents,
                config=types.GenerateContentConfig(
                    response_modalities=['TEXT', 'IMAGE'],
                    max_output_tokens=8192,  # Máximo de tokens para output detalhado
                    temperature=0.1,  # Baixa temperatura para consistência
                    candidate_count=1  # Uma única resposta de alta qualidade
                )
            )
            
            # Extrair a imagem gerada
            for part in response.candidates[0].content.parts:
                if part.inline_data is not None:
                    # Retornar imagem original sem processamento
                    return part.inline_data.data
            
            raise RuntimeError("Nenhuma imagem foi gerada na resposta")
            
        except Exception as e:
            error_message = str(e)
            
            # Se é erro 503 (overloaded) ou 500 (internal), tenta novamente após delay progressivo
            if any(code in error_message for code in ["503", "500", "overloaded", "internal"]):
                if attempt < max_retries - 1:
                    # Delay progressivo: 5s, 10s, 15s, 25s, 35s, 50s, 65s, 80s
                    base_delays = [5, 10, 15, 25, 35, 50, 65, 80]
                    delay = base_delays[min(attempt, len(base_delays) - 1)]
                    delay += random.uniform(-1, 3)
                    
                    time.sleep(delay)
                    continue
            
            # Para outros erros, falha imediatamente
            raise RuntimeError(f"Erro ao gerar imagem: {error_message}")
    
    # Se todas as tentativas falharam
    raise RuntimeError("Todas as tentativas de geração de imagem falharam")


def classificar_tipo_comodo(prompt: str) -> str:
    """
    Classifica o tipo de cômodo com base em descrição textual, usando o modelo de texto Gemini.
    
    Retorna apenas a string com o tipo (ex: 'quarto_casal', 'sala', etc.).
    """
    try:
        response = modelo_texto.generate_content(prompt)
        return response.text.strip().lower()
    except Exception as e:
        raise RuntimeError(f"Erro na classificação de cômodo: {str(e)}")


def interpretar_planta_com_imagem(prompt: str, image_bytes: bytes) -> str:
    """
    Interpreta uma planta baixa usando modelo multimodal do Gemini
    """
    try:
        # Preparar conteúdo multimodal
        contents = [
            {"mime_type": "image/png", "data": image_bytes},
            {"text": prompt}
        ]
        response = modelo_multimodal.generate_content(contents)
        return response.text
    except Exception as e:
        raise RuntimeError(f"Erro na interpretação da planta: {str(e)}")
