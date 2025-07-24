# mrv-house-plan

npx shadcn@latest add "https://v0.dev/chat/b/b_RVNL81kSSwh?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..66El7Dtw37YcbdnI.vPKd1uXUSyXVgDyDBVx700aAn4cJMfxixwL2eYWi_DTGtNlY6D84XHA0fEg.kiuta41bRtXvyU4S9uWQug"



pré processamento

        +---------------------------+
        |   Imagem da Planta       |
        | (JPG / PNG / PDF Upload) |
        +-----------+--------------+
                    |
                    v
        +---------------------------+
        |    OCR com Python         |
        | (Tesseract / EasyOCR)     |
        +-----------+--------------+
                    |
         Extração de textos brutos:
         - Nomes dos cômodos
         - Medidas (ex: 3,2m x 2,8m)
                    |
                    v
        +---------------------------+
        |  Montagem do Prompt       |
        |  para LLM                 |
        |  (Imagem + Texto extraído)|
        +-----------+--------------+
                    |
                    v
        +---------------------------+
        |      LLM (Gemini)         |
        | Interpretação semântica   |
        +-----------+--------------+
                    |
         Interpretação e estruturação:
         - Nome de cada cômodo
         - Dimensões e localização
         - Orientação no layout
                    |
                    v
        +---------------------------+
        |   Saída Estruturada       |
        |      (JSON)               |
        +---------------------------+

Exemplo de saída:
{
  "comodos": [
    {
      "nome": "Quarto",
      "largura_m": 3.2,
      "comprimento_m": 2.8,
      "posicao": "superior direita"
    },
    ...
  ]
}
