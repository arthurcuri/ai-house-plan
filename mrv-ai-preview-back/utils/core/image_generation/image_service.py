
from core.ai.gemini_service import gerar_imagem, classificar_tipo_comodo
import base64

def classificar_comodo(comodo: dict) -> str:
    prompt = f"""
Você é um assistente que classifica ambientes de uma planta arquitetônica residencial.

Com base nas seguintes informações:

- Nome do cômodo: {comodo["nome"]}
- Dimensões: {comodo["dimensões"]}
- Localização: {comodo["localização"]}

Classifique o tipo de cômodo, escolhendo **apenas uma das seguintes opções**:

- quarto_pequeno
- quarto_casal
- sala
- sala_cozinha
- banheiro
- área_privativa
- outro

Retorne **apenas o nome da opção** correspondente ao tipo do cômodo.
"""
    return classificar_tipo_comodo(prompt)

def gerar_prompt_essencial(comodo: dict) -> str:
    # Import locally to avoid circular imports
    from core.image_generation.prompts import (
        quarto_pequeno_essencial,
        quarto_casal_essencial, 
        sala_essencial,
        area_privativa_essencial
    )
    
    tipo = classificar_comodo(comodo)

    match tipo:
        case "quarto_pequeno":
            return quarto_pequeno_essencial(comodo)
        case "quarto_casal":
            return quarto_casal_essencial(comodo)
        case "sala":
            return sala_essencial(comodo)
        case "área_privativa":
            return area_privativa_essencial(comodo)
        case _:
            return f"""
Crie uma imagem 3D genérica para o cômodo '{comodo['nome']}' com dimensões {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm. 
Decoração simples no padrão ESSENCIAL da MRV.
"""

def gerar_imagens_para_comodos(lista_comodos: list[dict], imagem_planta_bytes: bytes) -> list[dict]:
    """
    Gera imagens com base nos cômodos e na planta original.
    Agora com compressão automática para reduzir o tamanho das respostas.
    """
    imagens = []

    for comodo in lista_comodos:
        try:
            prompt = gerar_prompt_essencial(comodo)
            # Usar compressão por padrão para reduzir o tamanho da resposta
            imagem = gerar_imagem(prompt, image_bytes=imagem_planta_bytes, compress=True)
            imagem_base64 = base64.b64encode(imagem).decode("utf-8")
            imagens.append({
                "comodo": comodo["nome"],
                "prompt": prompt,
                "imagem_base64": imagem_base64,
                "tamanho_bytes": len(imagem)
            })
        except Exception as e:
            imagens.append({
                "comodo": comodo.get("nome", "Desconhecido"),
                "erro": str(e)
            })

    return imagens