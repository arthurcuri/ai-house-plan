from fastapi import APIRouter, UploadFile, File, Form, Depends
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
from pathlib import Path
from ...auth.middleware import get_current_active_user
from ...auth.models import User
from ...database.db_service import get_db
from sqlalchemy.orm import Session
from ...database.architect_service import get_personal_type_by_id, get_room_prompts

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parents[3]
# Diretório para salvar as imagens geradas
IMAGES_OUTPUT_DIR = BASE_DIR / "generated_images"
IMAGES_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


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
    tipo: str = Form(None),
    tipo_pessoal_id: int = Form(None),
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    image_np = np.array(image)

    # ✅ VALIDAR TIPO DE APARTAMENTO OU TIPO PESSOAL
    tipo_para_interpretacao = None
    tipo_pessoal = None

    if tipo_pessoal_id:
        # Usuário escolheu tipo pessoal
        tipo_pessoal = get_personal_type_by_id(db, tipo_pessoal_id, current_user.id)
        
        if not tipo_pessoal:
            return {
                "erro": f"Tipo pessoal {tipo_pessoal_id} não encontrado ou você não tem permissão para acessá-lo"
            }
        
        if tipo_pessoal.status != "concluido":
            return {
                "erro": f"Tipo pessoal ainda está processando. Status: {tipo_pessoal.status}. Aguarde a conclusão da análise."
            }
        
        if not tipo_pessoal.prompts_gerados:
            return {
                "erro": f"Prompts do tipo pessoal ainda não foram gerados. Status: {tipo_pessoal.status}"
            }

        # Para interpretação, usar tipo fornecido ou 'essential' como fallback
        tipo_para_interpretacao = tipo.lower() if tipo else 'essential'

    elif tipo:
        # Usuário escolheu tipo padrão
        tipos_validos = ['essential', 'eco', 'bio', 'class']
        if tipo.lower() not in tipos_validos:
            return {
                "erro": f"Tipo de apartamento '{tipo}' inválido. Tipos permitidos: {tipos_validos}",
                "tipos_disponveis": tipos_validos
            }
        tipo_para_interpretacao = tipo.lower()
    else:
        # Nenhum tipo fornecido
        return {
            "erro": "É necessário fornecer 'tipo' (essential/eco/bio/class) ou 'tipo_pessoal_id'"
        }

    # ✅ OCR
    result = reader.readtext(image_np)
    textos_ocr = [r[1] for r in result]

    # ✅ Interpretação da planta via LLM
    try:
        dados = interpreter_plan.interpretar_planta_com_ocr(
            contents, 
            textos_ocr, 
            tipo_apartamento=tipo_para_interpretacao,
            tipo_pessoal_nome=None
        )
        comodos = dados.get("comodos") or dados.get("cômodos")
    except Exception as e:
        return {
            "erro": f"Erro ao interpretar a planta: {str(e)}",
            "detalhes": str(e) if hasattr(e, '__dict__') else None
        }

    if not comodos:
        return {"erro": "Nenhum cômodo encontrado na interpretação da planta."}

    # ✅ Configurações fixas em ULTRA ALTA QUALIDADE
    tipo_prompt_usado = f"tipo_pessoal_{tipo_pessoal_id}" if tipo_pessoal_id else tipo_para_interpretacao.upper()
    
    configuracao = {
        "alta_qualidade": True,
        "resolucao": "MÁXIMA DISPONÍVEL NO MODELO",
        "qualidade": "ULTRA ALTA DEFINIÇÃO - sem compressão",
        "rendering": "Fotorrealístico com ray tracing completo",
        "anti_aliasing": "Máximo",
        "max_tentativas": 8,
        "delay_progressivo": "5s até 80s",
        "formato": "PNG sem compressão",
        "tipo_prompt": tipo_prompt_usado
    }

    # ✅ SEMPRE GERAR ARQUIVOS EM ALTA QUALIDADE
    session_id = str(uuid.uuid4())[:8]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_dir = IMAGES_OUTPUT_DIR / f"{timestamp}_{session_id}"
    session_dir.mkdir(parents=True, exist_ok=True)

    imagens_info = []
    tipos_validos = ['essential', 'eco', 'bio', 'class']  # Definir aqui para usar no except
    
    for i, comodo in enumerate(comodos):
        try:
            if not isinstance(comodo, dict):
                raise ValueError(f"Expected 'comodo' to be a dictionary, got {type(comodo)}")
            
            # Gerar prompt específico para o cômodo
            from ...core.image_generation.image_service import gerar_prompt_por_tipo

            if tipo_pessoal_id:
                # USUÁRIO ESCOLHEU TIPO PESSOAL: usar prompts personalizados
                prompts_pessoais = get_room_prompts(db, tipo_pessoal_id)
                tipo_comodo = comodo.get('tipo', 'generico')
                prompt = prompts_pessoais.get(tipo_comodo)
                
                if not prompt:
                    # Fallback para prompt padrão se não encontrado
                    prompt = gerar_prompt_por_tipo(comodo, tipo_para_interpretacao.upper())
            else:
                # USUÁRIO ESCOLHEU TIPO PADRÃO: usar prompts padrão do tipo escolhido
                prompt = gerar_prompt_por_tipo(comodo, tipo_para_interpretacao.upper())
            
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
                "dimensoes": comodo.get("dimensoes", {}),
                "localizacao": comodo.get("localizacao", ""),
                "notas": comodo.get("notas", "")
            })
            
        except ValueError as e:
            return {
                "erro": str(e),
                "tipos_disponveis": tipos_validos if not tipo_pessoal_id else None
            }
        except Exception as e:
            imagens_info.append({
                "comodo": comodo.get("nome", "Desconhecido"),
                "erro": str(e)
            })

    return {
        "modo": "arquivos_hd",
        "tipo": tipo_prompt_usado,  # ← CORRIGIDO: usar tipo_prompt_usado ao invés de tipo.upper()
        "tipo_pessoal_id": tipo_pessoal_id if tipo_pessoal_id else None,
        "quantidade_comodos": len(comodos),
        "session_id": f"{timestamp}_{session_id}",
        "diretorio": session_dir,
        "configuracao": configuracao,
        "resultado": imagens_info
    }