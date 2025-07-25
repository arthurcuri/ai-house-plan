from prompt_factory import *
from llm_factory import gerar_imagem, classificar_tipo_comodo
import base64



def classificar_comodo(comodo:dict) -> str:

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
    
    return classificar_comodo(prompt)


def gerar_prompt_essencial(comodo: dict) -> str:
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
        
def gerar_imagens_para_comodos(lista_comodos: list[dict], imagem_planta_bytes: bytes,) -> list[dict]:
     """
    Gera imagens com base nos cômodos e na planta original.
    """
     
     imagens= []

     for comodo in lista_comodos:
         prompt = gerar_prompt_essencial(comodo)
         imagem = gerar_imagem(prompt, image_bytes=imagem_planta_bytes)
         imagem_base64 = base64.b64(imagem).decode("utf-8")
         imagens.append({
    "comodo": comodo["nome"],
    "prompt": prompt,
    "imagem_base64": imagem_base64
            })
         return imagens
     


     
