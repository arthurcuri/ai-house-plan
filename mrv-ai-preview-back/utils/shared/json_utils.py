# json_utils.py

import re
import json

def limpar_json_llm(entrada: str) -> dict:
    """
    Remove delimitadores markdown e retorna dict.
    """
    texto_limpo = re.sub(r"^```json|```$", "", entrada.strip()).strip()
    return json.loads(texto_limpo)
