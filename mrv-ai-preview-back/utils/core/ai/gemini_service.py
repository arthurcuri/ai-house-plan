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
    print("Gemini 2.0 não disponível, usando implementação alternativa")

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


def gerar_imagem(prompt: str, image_bytes: bytes = None, max_retries: int = 8, compress: bool = True) -> bytes:
    """
    Gera uma imagem usando Gemini 2.0 Flash Preview se disponível,
    caso contrário usa implementação alternativa.
    Requer uma imagem de referência e retorna tanto texto quanto imagem.
    
    Args:
        prompt: Descrição do que gerar
        image_bytes: Bytes da imagem de referência (planta)
        max_retries: Número máximo de tentativas em caso de erro 503/500 (padrão: 8)
        compress: Se deve comprimir a imagem para reduzir o tamanho
    """
    for attempt in range(max_retries):
        try:
            if GEMINI_2_AVAILABLE and image_bytes:
                # Preparar a entrada de texto com mais detalhes sobre dimensões
                text_input = f"""
                Baseado na planta arquitetônica fornecida, {prompt}
                
                IMPORTANTE SOBRE PROPORÇÕES: As dimensões reais deste cômodo foram extraídas da planta via OCR. 
                Use essas proporções APENAS para orientar o layout e distribuição dos móveis, não para alterar a resolução da imagem.
                
                ESPECIFICAÇÕES TÉCNICAS OBRIGATÓRIAS DA IMAGEM:
                - Resolução: EXATAMENTE 2048x2048 pixels (formato quadrado de alta definição)
                - Qualidade: Máxima possível do modelo Gemini
                - Formato: Quadrado independente das proporções do cômodo
                
                Gere uma imagem 3D fotorrealista de MÁXIMA QUALIDADE que represente fielmente:
                1. As proporções do cômodo conforme especificado (mas adapte para formato quadrado 2048x2048)
                2. O layout e distribuição de móveis adequados ao tamanho real do cômodo
                3. Iluminação natural realista com ray tracing global e sombras suaves
                4. Texturas ultra-detalhadas em alta definição (madeira, tecidos, metais, cerâmica, vidro)
                5. Cores vibrantes mas naturais com correção de cor cinematográfica
                6. Perspectiva arquitetônica profissional com profundidade de campo realista
                7. Materiais fotorrealistas com reflexos, refrações e brilhos naturais
                8. Qualidade de renderização cinematográfica com anti-aliasing máximo
                9. Detalhes finos como texturas de parede, grãos de madeira, fibras de tecido
                10. Composição arquitetônica perfeita enquadrada em formato quadrado
                
                IMPORTANTE: Mesmo que o cômodo seja retangular, enquadre a visualização em formato quadrado (2048x2048) 
                mostrando uma perspectiva que revele bem as proporções e características do ambiente.
                
                A imagem deve ser indistinguível de uma fotografia real de um ambiente construído, com qualidade de portfólio arquitetônico profissional.
                """
                
                # Converter bytes para PIL Image
                reference_image = Image.open(BytesIO(image_bytes))
                
                # Preparar conteúdo com imagem de referência
                contents = [text_input, reference_image]
                
                # Gerar conteúdo com o modelo de geração de imagens
                response = client.models.generate_content(
                    model="gemini-2.0-flash-preview-image-generation",
                    contents=contents,
                    config=types.GenerateContentConfig(
                        response_modalities=['TEXT', 'IMAGE']  # Ambos são necessários
                    )
                )
                
                # Extrair a imagem gerada
                for part in response.candidates[0].content.parts:
                    if part.inline_data is not None:
                        image_data = part.inline_data.data
                        
                        # Comprimir a imagem se solicitado
                        if compress:
                            image_data = _comprimir_imagem(image_data)
                        
                        return image_data
            
            # Se não há Gemini 2.0 disponível ou não há imagem de referência,
            # usa implementação placeholder elaborada
            return _gerar_imagem_placeholder(prompt, compress=compress)
            
        except Exception as e:
            error_message = str(e)
            print(f"Erro ao gerar imagem (tentativa {attempt + 1}/{max_retries}): {error_message}")
            
            # Se é erro 503 (overloaded) ou 500 (internal), tenta novamente após delay progressivo
            if any(code in error_message for code in ["503", "500", "overloaded", "internal"]):
                if attempt < max_retries - 1:  # Não esperar na última tentativa
                    # Delay progressivo: 5s, 10s, 15s, 25s, 35s, 50s, 65s, 80s
                    base_delays = [5, 10, 15, 25, 35, 50, 65, 80]
                    delay = base_delays[min(attempt, len(base_delays) - 1)]
                    # Adicionar pequena randomização para evitar thundering herd
                    delay += random.uniform(-1, 3)
                    
                    if "503" in error_message or "overloaded" in error_message.lower():
                        print(f"🔄 Modelo sobrecarregado, aguardando {delay:.1f}s antes da próxima tentativa...")
                    elif "500" in error_message or "internal" in error_message.lower():
                        print(f"⚠️  Erro interno do servidor, aguardando {delay:.1f}s antes da próxima tentativa...")
                    
                    print(f"⏱️  Tentativa {attempt + 2} de {max_retries} em breve...")
                    time.sleep(delay)
                    continue
            
            # Para outros erros, retorna placeholder imediatamente
            print(f"❌ Erro não recuperável, abortando: {error_message}")
            break
    
    # Se todas as tentativas falharam, retorna placeholder elaborado
    print("🎨 Todas as tentativas falharam, gerando placeholder elaborado em alta qualidade...")
    return _gerar_imagem_placeholder(prompt, compress=compress)


def _comprimir_imagem(image_data: bytes, quality: int = 100, max_size: tuple = (2048, 2048)) -> bytes:
    """
    Processa imagem em resolução 2048x2048 pixels mantendo qualidade máxima.
    """
    try:
        # Abrir a imagem
        image = Image.open(BytesIO(image_data))
        
        # Forçar exatamente 2048x2048 pixels (formato quadrado)
        target_width, target_height = max_size
        
        # Redimensionar para exatamente 2048x2048 mantendo a melhor qualidade
        # Usar LANCZOS que é o melhor algoritmo para redimensionamento
        image = image.resize((target_width, target_height), Image.Resampling.LANCZOS)
        
        # Salvar com qualidade máxima em PNG
        buffer = BytesIO()
        image.save(
            buffer, 
            format='PNG', 
            optimize=False  # Não otimizar para manter máxima qualidade
        )
        
        print(f"📐 Imagem processada: {image.size[0]}x{image.size[1]} pixels, formato PNG (máxima qualidade)")
        return buffer.getvalue()
        
    except Exception as e:
        print(f"Erro ao processar imagem: {e}")
        return image_data  # Retorna original em caso de erro


def _gerar_imagem_placeholder(prompt: str, compress: bool = True) -> bytes:
    """
    Gera uma imagem placeholder em resolução 2048x2048 baseada no prompt.
    """
    try:
        # Sempre usar 2048x2048 para consistência
        width, height = 2048, 2048
        
        print(f"🎨 Gerando placeholder {width}x{height} (qualidade máxima)...")
        
        # Determinar cor baseada no prompt
        if "quarto" in prompt.lower() or "dormitório" in prompt.lower():
            color = (173, 216, 230)  # Azul claro
        elif "sala" in prompt.lower():
            color = (255, 222, 173)  # Laranja claro
        elif "cozinha" in prompt.lower():
            color = (144, 238, 144)  # Verde claro
        elif "banho" in prompt.lower() or "banheiro" in prompt.lower():
            color = (230, 230, 250)  # Lavanda
        else:
            color = (245, 245, 245)  # Cinza claro
        
        # Criar imagem com gradiente mais sofisticado
        from PIL import ImageDraw, ImageFont, ImageFilter
        image = Image.new('RGB', (width, height), color)
        draw = ImageDraw.Draw(image)
        
        # Gradiente radial do centro para as bordas
        center_x, center_y = width // 2, height // 2
        max_distance = ((width/2)**2 + (height/2)**2)**0.5
        
        for y in range(height):
            for x in range(width):
                distance = ((x - center_x)**2 + (y - center_y)**2)**0.5
                alpha = distance / max_distance
                gradient_color = tuple(int(c * (0.9 + 0.1 * alpha)) for c in color)
                image.putpixel((x, y), gradient_color)
        
        # Adicionar texto indicativo mais elegante
        try:
            font_size = 96  # Tamanho proporcional para 2048x2048
            font = ImageFont.load_default()
        except:
            font = None
        
        text = "PLACEHOLDER - QUALIDADE MÁXIMA\n2048x2048 pixels - PNG"
        if font:
            # Calcular posição centralizada para texto multi-linha
            lines = text.split('\n')
            total_height = len(lines) * 120  # Proporcional ao novo tamanho
            start_y = (height - total_height) // 2
            
            for i, line in enumerate(lines):
                bbox = draw.textbbox((0, 0), line, font=font)
                text_width = bbox[2] - bbox[0]
                x = (width - text_width) // 2
                y = start_y + i * 120
                # Sombra do texto
                draw.text((x+4, y+4), line, fill=(50, 50, 50), font=font)
                # Texto principal
                draw.text((x, y), line, fill=(100, 100, 100), font=font)
        
        # Salvar em bytes com qualidade máxima em PNG
        buffer = BytesIO()
        image.save(
            buffer, 
            format='PNG',
            optimize=False
        )
        
        print(f"✅ Placeholder criado: {width}x{height}, {len(buffer.getvalue())} bytes (qualidade máxima PNG)")
        return buffer.getvalue()
        
    except Exception as e:
        print(f"Erro ao criar placeholder: {e}")
        # Se tudo falhar, retorna dados básicos
        return b"placeholder_image_data"


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

    