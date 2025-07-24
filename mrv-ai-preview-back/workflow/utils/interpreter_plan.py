from llm_factory import interpretar_planta_com_imagem

# ✅ Caminho absoluto da imagem da planta
CAMINHO_IMAGEM = r"C:\Users\lucas.nogueira\Documents\projetos_pessoais\mrv-ai\mrv-house-plan\mrv-ai-preview-back\workflow\planta01.jpg"

# ✅ OCR real extraído via EasyOCR
texto_ocr = [
    "QUARTO", "QUARTO", "240", "122", "120", "230",
    "140", "CIRC.", "192", "254", "140", "SALACOZINHAAS"
]

# ✅ Prompt estruturado para a LLM interpretar
prompt = f"""
Você é um assistente especialista em interpretação de plantas arquitetônicas residenciais.

Com base no seguinte texto extraído por OCR da planta:

{texto_ocr}

E considerando a imagem da planta fornecida, identifique com o máximo de precisão:

1. Quais são os cômodos presentes?
2. Quais são as dimensões aproximadas de cada um (em cm)?
3. Qual a localização relativa de cada cômodo (ex: 'superior esquerdo', 'centro', etc)?

Responda em formato JSON estruturado. Seja preciso e conciso.
"""

# ✅ Leitura da imagem como bytes
with open(CAMINHO_IMAGEM, "rb") as f:
    image_bytes = f.read()

# ✅ Chamada para a LLM
resposta = interpretar_planta_com_imagem(prompt, image_bytes)

# ✅ Resultado
print("🧠 Resposta da LLM:\n")
print(resposta)
