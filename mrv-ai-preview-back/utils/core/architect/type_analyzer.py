"""
Serviço para análise multimodal de fotos e geração de prompts personalizados
"""
from typing import List, Dict, Tuple
from PIL import Image
from io import BytesIO
import logging
from pydantic import ValidationError

logger = logging.getLogger(__name__)

# Lista de tipos de cômodos suportados (alinhado com image_service.py)
TIPOS_COMODOS = [
    "quarto_pequeno", "quarto_casal", "suite",
    "sala", "sala_cozinha",
    "cozinha", "banheiro",
    "varanda", "sacada", "lavanderia",
    "escritorio", "home_office", "closet",
    "corredor", "hall",
    "area_privativa", "area_gourmet",
    "generico"  # Alinhado com image_service.py
]

def _carregar_exemplo_prompt_padrao(tipo_comodo: str) -> str:
    """
    Carrega um exemplo de prompt padrão (ESSENTIAL) para usar como referência.
    Isso garante que a LLM gere prompts no mesmo formato e estrutura.
    """
    try:
        from ...image_generation.prompt_essential import (
            quarto_pequeno_essential, quarto_casal_essential, sala_essential,
            area_privativa_essential, banheiro_essential, cozinha_essential, 
            varanda_essential, generico_essential, lavanderia_essential,
            escritorio_essential, closet_essential, suite_essential,
            corredor_essential, hall_essential, sacada_essential,
            area_gourmet_essential, home_office_essential
        )
        
        # Mapeamento de tipos para funções
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
        
        # Criar um cômodo exemplo para gerar o prompt de referência
        comodo_exemplo = {
            'dimensões': {'largura': 300, 'comprimento': 400},
            'localização': 'center',
            'notas': 'Example room layout and furniture arrangement'
        }
        
        # Obter função correspondente
        prompt_function = prompt_functions.get(tipo_comodo, generico_essential)
        
        # Gerar prompt de exemplo
        prompt_exemplo = prompt_function(comodo_exemplo)
        
        return prompt_exemplo
        
    except Exception as e:
        logger.warning(f"Erro ao carregar prompt padrão: {e}")
        return None

def analisar_fotos_e_gerar_prompts(
    fotos_bytes: List[bytes],
    nome_tipo: str
) -> Tuple[Dict[str, str], str]:
    """
    Analisa múltiplas fotos de projetos e gera prompts personalizados
    para cada tipo de cômodo baseado no estilo identificado.
    Usa structured output e referencia prompts padrão para manter formato.
    """
    try:
        from ..ai.gemini_service import client, modelo_multimodal
        from ..ai.schemas import AnaliseEstiloArquitetura
        from google.genai import types
        
        # Preparar imagens PIL
        imagens = []
        for foto_bytes in fotos_bytes:
            img = Image.open(BytesIO(foto_bytes))
            if img.mode != 'RGB':
                img = img.convert('RGB')
            imagens.append(img)
        
        # Carregar exemplo de prompt padrão para referência
        exemplo_prompt = _carregar_exemplo_prompt_padrao("sala")
        
        # Construir prompt de análise com referência ao formato padrão
        prompt_analise = f"""
        Analise as seguintes fotos de projetos arquitetônicos reais e identifique o estilo arquitetônico comum entre elas.

        Nome do estilo: {nome_tipo}

        Analise:
        1. Estilo arquitetônico predominante
        2. Paleta de cores comum
        3. Materiais e acabamentos
        4. Estilo de mobiliário
        5. Iluminação e atmosfera
        6. Elementos decorativos característicos

        Com base nessa análise, gere prompts personalizados para CADA um dos seguintes tipos de cômodos:
        {', '.join(TIPOS_COMODOS)}

        IMPORTANTE: Mantenha EXATAMENTE a mesma estrutura e formato dos prompts padrão. Use o seguinte exemplo como referência:

        --- EXEMPLO DE PROMPT PADRÃO (formato a seguir) ---
        {exemplo_prompt if exemplo_prompt else "Formato padrão não disponível"}
        --- FIM DO EXEMPLO ---

        Para cada cômodo, crie um prompt que:
        - Use a MESMA estrutura do exemplo acima (dimensões, localização, notas, descrição detalhada)
        - Substitua o estilo MRV ESSENTIAL pelo estilo identificado nas fotos ({nome_tipo})
        - Mantenha a formatação e organização do texto
        - Seja específico sobre cores, materiais, mobiliário e decoração do estilo identificado
        - Seja fotorrealístico e detalhado
        - Use inglês para o prompt final
        - Inclua placeholders {{comodo['dimensões']['largura']}}, {{comodo['dimensões']['comprimento']}}, {{comodo['localização']}}, {{comodo.get('notas')}} que serão substituídos dinamicamente
        """
        
        # Preparar conteúdo multimodal
        contents = [prompt_analise] + imagens
        
        # Schema para structured output
        schema = AnaliseEstiloArquitetura
        
        # Chamar Gemini com structured output
        response = client.models.generate_content(
            model=modelo_multimodal,
            contents=contents,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=schema.model_json_schema(),
            )
        )
        
        # Parse e validação automática com Pydantic
        resultado = schema.model_validate_json(response.text)
        
        # Extrair dados
        prompts_dict = resultado.prompts
        analise_estilo = resultado.analise_estilo
        
        # Garantir que todos os tipos de cômodos tenham prompt
        for tipo_comodo in TIPOS_COMODOS:
            if tipo_comodo not in prompts_dict:
                prompts_dict[tipo_comodo] = f"Create a photorealistic 3D image of a {tipo_comodo} in the style of {nome_tipo}."
        
        return prompts_dict, analise_estilo
        
    except ValidationError as e:
        logger.error(f"Erro de validação do schema: {e}")
        raise RuntimeError(f"Resposta do modelo não corresponde ao schema esperado: {e}")
    except Exception as e:
        logger.error(f"Erro ao analisar fotos: {e}")
        raise RuntimeError(f"Erro na análise LLM: {str(e)}")