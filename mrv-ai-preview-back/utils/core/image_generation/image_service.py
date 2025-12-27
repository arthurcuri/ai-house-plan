

from core.ai.gemini_service import gerar_imagem
import base64


def _normalizar_comodo(comodo: dict) -> dict:
    """
    Normaliza o dicionário do cômodo para compatibilidade com prompts.
    Converte campos sem acento (do schema) para com acento (esperado pelos prompts).
    """
    comodo_normalizado = comodo.copy()
    
    # Normalizar dimensões
    if 'dimensoes' in comodo_normalizado and 'dimensões' not in comodo_normalizado:
        dimensoes = comodo_normalizado['dimensoes']
        
        # Se for dict (já convertido do Pydantic)
        if isinstance(dimensoes, dict):
            comodo_normalizado['dimensões'] = {
                'largura': dimensoes.get('largura_cm', 0),
                'comprimento': dimensoes.get('comprimento_cm', 0),
                'largura_m': dimensoes.get('largura_m', 0),
                'comprimento_m': dimensoes.get('comprimento_m', 0)
            }
        # Se for objeto Pydantic (ainda não convertido)
        else:
            comodo_normalizado['dimensões'] = {
                'largura': getattr(dimensoes, 'largura_cm', 0),
                'comprimento': getattr(dimensoes, 'comprimento_cm', 0),
                'largura_m': getattr(dimensoes, 'largura_m', 0),
                'comprimento_m': getattr(dimensoes, 'comprimento_m', 0)
            }
    
    # Normalizar localização
    if 'localizacao' in comodo_normalizado and 'localização' not in comodo_normalizado:
        comodo_normalizado['localização'] = comodo_normalizado.get('localizacao', '')
    
    return comodo_normalizado


def gerar_prompt_por_tipo(comodo: dict, tipo_apartamento: str) -> str:
    """
    Gera prompt específico baseado no tipo do apartamento e tipo do cômodo.
    Usa o tipo já classificado na análise unificada (structured output).
    """
    tipo_apartamento = tipo_apartamento.upper()
    tipo_comodo = comodo.get('tipo', 'outro')
    
    # Normalizar tipo (remover acentos para compatibilidade)
    tipo_comodo = tipo_comodo.replace('área_privativa', 'area_privativa')
    
    # Validar tipos permitidos
    tipos_validos = ['ESSENTIAL', 'ECO', 'BIO', 'CLASS']
    if tipo_apartamento not in tipos_validos:
        raise ValueError(f"Tipo de apartamento '{tipo_apartamento}' inválido. Tipos permitidos: {tipos_validos}")
    
    # Normalizar comodo para compatibilidade com prompts
    comodo_normalizado = _normalizar_comodo(comodo)
    
    # Importar o módulo correto baseado no tipo
    if tipo_apartamento == 'ESSENTIAL':
        from core.image_generation.prompt_essential import (
            quarto_pequeno_essential, quarto_casal_essential, sala_essential,
            area_privativa_essential, banheiro_essential, cozinha_essential, 
            varanda_essential, generico_essential, lavanderia_essential,
            escritorio_essential, closet_essential, suite_essential,
            corredor_essential, hall_essential, sacada_essential,
            area_gourmet_essential, home_office_essential
        )
        prompt_functions = {
            "quarto_pequeno": quarto_pequeno_essential,
            "quarto_casal": quarto_casal_essential,
            "sala": sala_essential,
            "sala_cozinha": sala_essential,
            "area_privativa": area_privativa_essential,
            "banheiro": banheiro_essential,
            "cozinha": cozinha_essential,
            "varanda": varanda_essential,
            "lavanderia": lavanderia_essential,
            "escritorio": escritorio_essential,
            "closet": closet_essential,
            "suite": suite_essential,
            "corredor": corredor_essential,
            "hall": hall_essential,
            "sacada": sacada_essential,
            "area_gourmet": area_gourmet_essential,
            "home_office": home_office_essential,
            "generico": generico_essential
        }
    
    elif tipo_apartamento == 'ECO':
        from core.image_generation.prompt_eco import (
            quarto_pequeno_eco, quarto_casal_eco, sala_eco,
            area_privativa_eco, banheiro_eco, cozinha_eco, generico_eco,
            varanda_eco, lavanderia_eco, escritorio_eco, closet_eco,
            suite_eco, corredor_eco, hall_eco, sacada_eco,
            area_gourmet_eco, home_office_eco
        )
        prompt_functions = {
            "quarto_pequeno": quarto_pequeno_eco,
            "quarto_casal": quarto_casal_eco,
            "sala": sala_eco,
            "sala_cozinha": sala_eco,
            "area_privativa": area_privativa_eco,
            "banheiro": banheiro_eco,
            "cozinha": cozinha_eco,
            "varanda": varanda_eco,
            "lavanderia": lavanderia_eco,
            "escritorio": escritorio_eco,
            "closet": closet_eco,
            "suite": suite_eco,
            "corredor": corredor_eco,
            "hall": hall_eco,
            "sacada": sacada_eco,
            "area_gourmet": area_gourmet_eco,
            "home_office": home_office_eco,
            "generico": generico_eco
        }
    
    elif tipo_apartamento == 'BIO':
        from core.image_generation.prompt_bio import (
            quarto_pequeno_bio, quarto_casal_bio, sala_bio,
            area_privativa_bio, banheiro_bio, cozinha_bio, generico_bio,
            varanda_bio, lavanderia_bio, escritorio_bio, closet_bio,
            suite_bio, corredor_bio, hall_bio, sacada_bio,
            area_gourmet_bio, home_office_bio
        )
        prompt_functions = {
            "quarto_pequeno": quarto_pequeno_bio,
            "quarto_casal": quarto_casal_bio,
            "sala": sala_bio,
            "sala_cozinha": sala_bio,
            "area_privativa": area_privativa_bio,
            "banheiro": banheiro_bio,
            "cozinha": cozinha_bio,
            "varanda": varanda_bio,
            "lavanderia": lavanderia_bio,
            "escritorio": escritorio_bio,
            "closet": closet_bio,
            "suite": suite_bio,
            "corredor": corredor_bio,
            "hall": hall_bio,
            "sacada": sacada_bio,
            "area_gourmet": area_gourmet_bio,
            "home_office": home_office_bio,
            "generico": generico_bio
        }
    
    elif tipo_apartamento == 'CLASS':
        from core.image_generation.prompt_class import (
            quarto_pequeno_class, quarto_casal_class, sala_class,
            area_privativa_class, banheiro_class, cozinha_class, generico_class,
            varanda_class, lavanderia_class, escritorio_class, closet_class,
            suite_class, corredor_class, hall_class, sacada_class,
            area_gourmet_class, home_office_class
        )
        prompt_functions = {
            "quarto_pequeno": quarto_pequeno_class,
            "quarto_casal": quarto_casal_class,
            "sala": sala_class,
            "sala_cozinha": sala_class,
            "area_privativa": area_privativa_class,
            "banheiro": banheiro_class,
            "cozinha": cozinha_class,
            "varanda": varanda_class,
            "lavanderia": lavanderia_class,
            "escritorio": escritorio_class,
            "closet": closet_class,
            "suite": suite_class,
            "corredor": corredor_class,
            "hall": hall_class,
            "sacada": sacada_class,
            "area_gourmet": area_gourmet_class,
            "home_office": home_office_class,
            "generico": generico_class
        }
    
    # Buscar função correspondente ao tipo de cômodo
    prompt_function = prompt_functions.get(tipo_comodo, prompt_functions["generico"])
    
    return prompt_function(comodo_normalizado)


def gerar_imagens_para_comodos(lista_comodos: list[dict], imagem_planta_bytes: bytes, tipo_apartamento: str) -> list[dict]:
    """
    Gera imagens com base nos cômodos e na planta original.
    """
    import traceback
    imagens = []

    for i, comodo in enumerate(lista_comodos):
        try:
            prompt = gerar_prompt_por_tipo(comodo, tipo_apartamento)
            
            imagem = gerar_imagem(prompt, image_bytes=imagem_planta_bytes)
            
            imagem_base64 = base64.b64encode(imagem).decode("utf-8")
            imagens.append({
                "comodo": comodo["nome"],
                "prompt": prompt,
                "imagem_base64": imagem_base64,
                "tamanho_bytes": len(imagem),
                "tipo_apartamento": tipo_apartamento.upper()
            })
            
        except Exception as e:
            traceback.print_exc()
            
            imagens.append({
                "comodo": comodo.get("nome", "Desconhecido"),
                "erro": str(e)
            })

    return imagens








def classificar_comodo(comodo: dict) -> str:
    prompt = f"""
    [DEPRECATED]
You are an assistant that classifies rooms from a residential architectural floor plan.

Based on the following information:

- Nome do cômodo: {comodo["nome"]}
- Dimensões: {comodo["dimensões"]}
- Localização: {comodo["localização"]}

Classify the type of room, choosing **only one of the following options**:

- quarto_pequeno
- quarto_casal
- sala
- sala_cozinha
- banheiro
- cozinha
- área_privativa
- generico

Return **only the name of the option** corresponding to the room type.
"""

    return classificar_tipo_comodo(prompt)