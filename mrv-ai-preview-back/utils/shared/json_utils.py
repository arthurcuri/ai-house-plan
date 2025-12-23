# json_utils.py
import re
import json
import logging

def limpar_json_llm(entrada: str) -> dict:
    """
    Remove delimitadores markdown e retorna dict.
    [DEPRECATED] Com structured output, isso não é mais necessário na maioria dos casos.
    Mantido para fallback.
    """
    try:
        texto_limpo = re.sub(r"^|```$", "", entrada.strip()).strip()
        texto_limpo = re.sub(r"^```|```$", "", texto_limpo).strip()
        return json.loads(texto_limpo)
    except json.JSONDecodeError as e:
        logging.error(f"Erro ao parsear JSON: {e}")
        logging.error(f"Texto recebido: {entrada[:500]}")
        raise ValueError(f"JSON inválido: {e}")## 5. Atualizar rota para usar dados estruturados