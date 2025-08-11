
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
- cozinha
- área_privativa
- outro

Retorne **apenas o nome da opção** correspondente ao tipo do cômodo.
"""
    return classificar_tipo_comodo(prompt)

def gerar_prompt_por_tipo(comodo: dict, tipo_apartamento: str) -> str:
    """
    Gera prompt específico baseado no tipo do apartamento (ESSENTIAL, ECO, BIO, CLASS)
    e no tipo do cômodo detectado.
    
    Args:
        comodo: Dados do cômodo (nome, dimensões, localização)
        tipo_apartamento: ESSENTIAL, ECO, BIO ou CLASS
    
    Returns:
        Prompt específico para o tipo de apartamento e cômodo
        
    Raises:
        ValueError: Se o tipo de apartamento não for válido
    """
    tipo_apartamento = tipo_apartamento.upper()
    tipo_comodo = classificar_comodo(comodo)
    
    # Validar tipos permitidos
    tipos_validos = ['ESSENTIAL', 'ECO', 'BIO', 'CLASS']
    if tipo_apartamento not in tipos_validos:
        raise ValueError(f"Tipo de apartamento '{tipo_apartamento}' inválido. Tipos permitidos: {tipos_validos}")
    
    # Importar o módulo correto baseado no tipo
    if tipo_apartamento == 'ESSENTIAL':
        from core.image_generation.prompt_essential import (
            quarto_pequeno_essential, quarto_casal_essential, sala_essential,
            area_privativa_essential, banheiro_essential, cozinha_essential, varanda_essential, generico_essential
        )
        prompt_functions = {
            "quarto_pequeno": quarto_pequeno_essential,
            "quarto_casal": quarto_casal_essential,
            "sala": sala_essential,
            "sala_cozinha": sala_essential,  # Usar mesmo prompt da sala
            "área_privativa": area_privativa_essential,
            "banheiro": banheiro_essential,
            "cozinha": cozinha_essential,
            "varanda": varanda_essential,  
            "outro": generico_essential
            
        }
    
    elif tipo_apartamento == 'ECO':
        from core.image_generation.prompt_eco import (
            quarto_pequeno_eco, quarto_casal_eco, sala_eco,
            area_privativa_eco, banheiro_eco, cozinha_eco, generico_eco
        )
        prompt_functions = {
            "quarto_pequeno": quarto_pequeno_eco,
            "quarto_casal": quarto_casal_eco,
            "sala": sala_eco,
            "sala_cozinha": sala_eco,
            "área_privativa": area_privativa_eco,
            "banheiro": banheiro_eco,
            "cozinha": cozinha_eco,
            "outro": generico_eco
        }
    
    elif tipo_apartamento == 'BIO':
        from core.image_generation.prompt_bio import (
            quarto_pequeno_bio, quarto_casal_bio, sala_bio,
            area_privativa_bio, banheiro_bio, cozinha_bio, generico_bio
        )
        prompt_functions = {
            "quarto_pequeno": quarto_pequeno_bio,
            "quarto_casal": quarto_casal_bio,
            "sala": sala_bio,
            "sala_cozinha": sala_bio,
            "área_privativa": area_privativa_bio,
            "banheiro": banheiro_bio,
            "cozinha": cozinha_bio,
            "outro": generico_bio
        }
    
    elif tipo_apartamento == 'CLASS':
        from core.image_generation.prompt_class import (
            quarto_pequeno_class, quarto_casal_class, sala_class,
            area_privativa_class, banheiro_class, cozinha_class, generico_class
        )
        prompt_functions = {
            "quarto_pequeno": quarto_pequeno_class,
            "quarto_casal": quarto_casal_class,
            "sala": sala_class,
            "sala_cozinha": sala_class,
            "área_privativa": area_privativa_class,
            "banheiro": banheiro_class,
            "cozinha": cozinha_class,
            "outro": generico_class
        }
    
    # Buscar função correspondente ao tipo de cômodo
    prompt_function = prompt_functions.get(tipo_comodo, prompt_functions["outro"])
    
    return prompt_function(comodo)

def gerar_imagens_para_comodos(lista_comodos: list[dict], imagem_planta_bytes: bytes, tipo_apartamento: str = 'ESSENTIAL') -> list[dict]:
    """
    Gera imagens com base nos cômodos e na planta original.
    Agora com suporte aos 4 tipos de apartamento e compressão automática.
    
    Args:
        lista_comodos: Lista de cômodos detectados
        imagem_planta_bytes: Bytes da imagem da planta
        tipo_apartamento: Tipo do apartamento (ESSENTIAL, ECO, BIO, CLASS)
    
    Returns:
        Lista com imagens em base64 e metadados
    """
    imagens = []

    for comodo in lista_comodos:
        try:
            # Usar a função genérica que suporta todos os tipos
            prompt = gerar_prompt_por_tipo(comodo, tipo_apartamento)
            # Usar compressão por padrão para reduzir o tamanho da resposta
            imagem = gerar_imagem(prompt, image_bytes=imagem_planta_bytes, compress=True)
            imagem_base64 = base64.b64encode(imagem).decode("utf-8")
            imagens.append({
                "comodo": comodo["nome"],
                "prompt": prompt,
                "imagem_base64": imagem_base64,
                "tamanho_bytes": len(imagem),
                "tipo_apartamento": tipo_apartamento.upper()
            })
        except Exception as e:
            imagens.append({
                "comodo": comodo.get("nome", "Desconhecido"),
                "erro": str(e)
            })

    return imagens