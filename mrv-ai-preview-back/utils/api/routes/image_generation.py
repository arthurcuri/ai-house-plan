from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from PIL import Image
import io
import numpy as np
import json
import os
import uuid
import re
from datetime import datetime
from ...core.ocr.ocr_service import reader
from ...core.ai import interpreter_plan
from ...core.image_generation.image_service import gerar_imagens_para_comodos
from ...shared.json_utils import limpar_json_llm

router = APIRouter()

# Diretório para salvar as imagens geradas
IMAGES_OUTPUT_DIR = "/tmp/generated_images"
os.makedirs(IMAGES_OUTPUT_DIR, exist_ok=True)


def sanitizar_nome_arquivo(nome: str) -> str:
    """
    Sanitiza nome de arquivo removendo caracteres problemáticos.
    
    Args:
        nome: Nome original do cômodo
    
    Returns:
        Nome sanitizado seguro para usar como nome de arquivo
    """
    # Remover ou substituir caracteres problemáticos
    nome_limpo = nome.replace('/', '_')  # Barras viram underscores
    nome_limpo = nome_limpo.replace('\\', '_')  # Barras invertidas também
    nome_limpo = nome_limpo.replace(' ', '_')  # Espaços viram underscores
    nome_limpo = nome_limpo.replace(':', '_')  # Dois pontos
    nome_limpo = nome_limpo.replace('?', '_')  # Interrogação
    nome_limpo = nome_limpo.replace('*', '_')  # Asterisco
    nome_limpo = nome_limpo.replace('<', '_')  # Menor que
    nome_limpo = nome_limpo.replace('>', '_')  # Maior que
    nome_limpo = nome_limpo.replace('|', '_')  # Pipe
    nome_limpo = nome_limpo.replace('"', '_')  # Aspas duplas
    
    # Remover underscores múltiplos consecutivos
    nome_limpo = re.sub(r'_+', '_', nome_limpo)
    
    # Remover underscores no início e fim
    nome_limpo = nome_limpo.strip('_')
    
    # Converter para lowercase para consistência
    nome_limpo = nome_limpo.lower()
    
    # Se o nome ficou vazio após sanitização, usar fallback
    if not nome_limpo:
        nome_limpo = "comodo_sem_nome"
    
    return nome_limpo

@router.post("/gerar-imagens")
async def gerar_imagens(
    file: UploadFile = File(...), 
    tipo: str = Form(...)
):
    contents = await file.read()
    # Manter os bytes originais para máxima qualidade na geração de imagens
    # Converter para numpy array apenas para OCR, sem afetar a qualidade original
    image = Image.open(io.BytesIO(contents))
    image_np = np.array(image)

    # ✅ VALIDAR TIPO DE APARTAMENTO
    tipos_validos = ['essential', 'eco', 'bio', 'class']
    if tipo.lower() not in tipos_validos:
        return {
            "erro": f"Tipo de apartamento '{tipo}' inválido. Tipos permitidos: {tipos_validos}",
            "tipos_disponveis": tipos_validos
        }

    # ✅ OCR
    result = reader.readtext(image_np)
    textos_ocr = [r[1] for r in result]

    # ✅ Interpretação da planta via LLM
    try:
        interpretacao_raw = interpreter_plan.interpretar_planta_com_ocr(contents, textos_ocr, tipo)
        dados = limpar_json_llm(interpretacao_raw)
    except Exception as e:
        return {
            "erro": f"Erro ao interpretar a planta ou ao decodificar JSON: {str(e)}",
            "interpretacao_raw": interpretacao_raw if 'interpretacao_raw' in locals() else None
        }

    comodos = dados.get("cômodos") or dados.get("comodos")  # aceitar ambos formatos

    if not comodos:
        return {"erro": "Nenhum cômodo encontrado na interpretação da planta."}

    # ✅ Configurações fixas em ULTRA ALTA QUALIDADE
    configuracao = {
        "alta_qualidade": True,
        "resolucao": "MÁXIMA DISPONÍVEL NO MODELO",
        "qualidade": "ULTRA ALTA DEFINIÇÃO - sem compressão",
        "rendering": "Fotorrealístico com ray tracing completo",
        "anti_aliasing": "Máximo",
        "max_tentativas": 8,
        "delay_progressivo": "5s até 80s",
        "formato": "PNG sem compressão",
        "tipo_prompt": tipo.upper()
    }

    # ✅ SEMPRE GERAR ARQUIVOS EM ALTA QUALIDADE
    session_id = str(uuid.uuid4())[:8]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_dir = os.path.join(IMAGES_OUTPUT_DIR, f"{timestamp}_{session_id}")
    os.makedirs(session_dir, exist_ok=True)
    
    imagens_info = []
    
    for i, comodo in enumerate(comodos):
        try:
            # Ensure 'comodo' is a dictionary
            if not isinstance(comodo, dict):
                raise ValueError(f"Expected 'comodo' to be a dictionary, got {type(comodo)}")
            
            # Gerar prompt específico para o cômodo baseado no tipo do apartamento
            from ...core.image_generation.image_service import gerar_prompt_por_tipo
            prompt = gerar_prompt_por_tipo(comodo, tipo.upper())
            
            # Gerar imagem sempre em ULTRA ALTA QUALIDADE
            from ...core.ai.gemini_service import gerar_imagem
            image_data = gerar_imagem(prompt, image_bytes=contents)
            
            # Salvar em arquivo
            nome_sanitizado = sanitizar_nome_arquivo(comodo['nome'])
            filename = f"comodo_{i+1}_{nome_sanitizado}.png"
            filepath = os.path.join(session_dir, filename)
            
            with open(filepath, 'wb') as f:
                f.write(image_data)
            
            imagens_info.append({
                "comodo": comodo["nome"],
                "prompt": prompt,
                "arquivo": filepath,
                "tamanho_bytes": len(image_data),
                "url_relativa": f"/imagens/{timestamp}_{session_id}/{filename}",
                "dimensoes": comodo.get("dimensões", {}),
                "localizacao": comodo.get("localização", ""),
                "notas": comodo.get("notas", "")  # Add this line to include the 'notas' field
            })
            
        except ValueError as e:
            # Erro de validação de tipo
            return {
                "erro": str(e),
                "tipos_disponveis": tipos_validos
            }
        except Exception as e:
            imagens_info.append({
                "comodo": comodo.get("nome", "Desconhecido"),
                "erro": str(e)
            })

    return {
        "modo": "arquivos_hd",
        "tipo": tipo.upper(),
        "quantidade_comodos": len(comodos),
        "session_id": f"{timestamp}_{session_id}",
        "diretorio": session_dir,
        "configuracao": configuracao,
        "resultado": imagens_info
    }
