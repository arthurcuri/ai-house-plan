# PROMPTS ESSENTIAL - Padrão básico e funcional da MRV

# QUARTO PEQUENO ESSENTIAL
def quarto_pequeno_essential(comodo):
    return f"""
Crie uma imagem 3D fotorrealista de um quarto pequeno com aproximadamente {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, localizado na região {comodo['localização']} da planta.

O campo {comodo['notas']} indica os moveis, suas respectivas disposições e decoração observados na planta. Serão úteis para compor a imagem de forma mais precisa.

Este cômodo deve seguir o padrão ESSENTIAL da MRV, com foco em funcionalidade e acabamento simples. Considere as seguintes características observadas nas imagens de referência:

- Camas de solteiro: pode ser uma ou duas, lado a lado ou beliche, com roupa de cama neutra e colchas claras ou acinzentadas.
- Armários simples de MDF branco ou amadeirado, embutidos ou com portas lisas.
- Escrivaninha compacta ou bancada de estudos sob a janela, com cadeira simples (estilo escritório ou Eames branca).
- Decoração infantil ou juvenil discreta: prateleiras com livros, brinquedos, quadros temáticos (animais, frases).
- Paredes com pintura bicolor (verde-claro, cinza ou bege) ou papel de parede com bolinhas.
- Iluminação natural generosa vinda de janela lateral com persiana ou cortina leve.
- Piso laminado ou vinílico de cor clara ou amadeirada suave.

O ambiente deve transmitir praticidade e conforto, ideal para crianças ou adolescentes, com móveis funcionais e decoração econômica.
"""

# QUARTO CASAL ESSENTIAL
def quarto_casal_essential(comodo):
    return f"""
Crie uma imagem 3D realista de um quarto de casal com aproximadamente {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, localizado na região {comodo['localização']} da planta.

O campo {comodo['notas']} indica os moveis, suas respectivas disposições e decoração observados na planta. Serão úteis para compor a imagem de forma mais precisa.

O cômodo deve seguir o padrão ESSENTIAL da MRV, com decoração simples, confortável e funcional. Considere os seguintes elementos baseados nas imagens de referência:

- Cama de casal centralizada, com cabeceira estofada ou ripada em tom verde, bege ou ratan.
- Roupa de cama clara, mantas sobrepostas (verde oliva, nude, bege).
- Armário embutido de MDF amadeirado com portas lisas ou ripadas.
- Cortinas longas e finas em tom off-white.
- Paredes neutras ou com pintura bicolor (ex: verde musgo, terracota, bege claro).
- TV na parede oposta à cama, prateleiras ou nichos com decoração leve.
- Piso vinílico ou laminado em madeira clara.
- Iluminação natural ampla com entrada de luz lateral.

A decoração deve ser econômica, acolhedora e coerente com o padrão de acabamento mais básico da MRV, priorizando praticidade e estética suave.
"""

# SALA ESSENTIAL
def sala_essential(comodo):
    return f"""
Crie uma imagem 3D realista de uma sala de estar e jantar integradas com aproximadamente {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, localizada na região {comodo['localização']} da planta.

O campo {comodo['notas']} indica os moveis, suas respectivas disposições e decoração observados na planta. Serão úteis para compor a imagem de forma mais precisa.

A decoração deve seguir o padrão ESSENTIAL da MRV, com foco em ambientes simples, acolhedores e funcionais. Baseie-se nas seguintes referências:

- Sofá reto de 2 a 3 lugares, em tom claro (bege, areia ou cinza), com almofadas terrosas ou verdes.
- Painel de TV ou rack ripado em MDF amadeirado simples.
- Tapete claro e liso, cobrindo parcialmente a área da sala.
- TV de tela plana instalada na parede oposta ao sofá.
- Mesa de jantar compacta para 2 ou 4 lugares, com cadeiras em madeira ou palha.
- Parede de fundo com cor neutra ou destaque (verde musgo, terracota, cinza).
- Decoração leve com vasos de planta, luminária de canto, espelhos ou nichos decorativos.
- Piso vinílico ou laminado amadeirado claro.
- Iluminação natural abundante vinda de janelas com cortinas translúcidas.

A proposta deve transmitir um espaço contemporâneo, funcional e bem iluminado, adequado ao padrão de acabamento econômico da MRV.
"""

# ÁREA PRIVATIVA ESSENTIAL
def area_privativa_essential(comodo):
    return f"""
Crie uma imagem 3D fotorrealista de uma área privativa externa com aproximadamente {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, localizada na parte externa do apartamento, seguindo o padrão ESSENTIAL da MRV.

O campo {comodo['notas']} indica os moveis, suas respectivas disposições e decoração observados na planta. Serão úteis para compor a imagem de forma mais precisa.

Considere as seguintes referências extraídas das imagens:

- Piso parcialmente gramado (natural ou sintético) com áreas de concreto.
- Mesa redonda pequena com 2 a 4 cadeiras simples, em material metálico, plástico ou madeira.
- Plantas decorativas em vasos nos cantos ou ao longo dos muros.
- Parede de fundo lisa em tom areia ou branco, com acabamento simples.
- Iluminação natural generosa e, se for noturna, incluir iluminação de jardim embutida ou poste externo moderno.
- Itens decorativos simples: banco de madeira com almofadas, puffs, espreguiçadeiras ou casinha de cachorro.
- Aparência organizada, funcional e convidativa, sem excessos.

O ambiente deve transmitir uma área de lazer íntima e econômica, ideal para relaxar ou acomodar pequenos momentos ao ar livre.
"""

# BANHEIRO ESSENTIAL
def banheiro_essential(comodo):
    return f"""
Crie uma imagem 3D fotorrealista de um banheiro com aproximadamente {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, localizado na região {comodo['localização']} da planta.

O campo {comodo['notas']} indica os moveis, suas respectivas disposições e decoração observados na planta. Serão úteis para compor a imagem de forma mais precisa.

O cômodo deve seguir o padrão ESSENTIAL da MRV, com acabamento simples e funcional:

- Vaso sanitário branco convencional, com caixa acoplada.
- Pia simples de louça branca com bancada em granito ou mármore básico.
- Chuveiro com registro simples, sem ducha ou hidromassagem.
- Revestimento básico: azulejos brancos ou bege até meia altura, tinta acima.
- Piso cerâmico antiderrapante em tons neutros (branco, bege, cinza claro).
- Espelho simples retangular sobre a pia.
- Iluminação básica com uma lâmpada central ou arandela simples.
- Toalhas em tons claros, sabonete líquido, papel higiênico.

O ambiente deve ser limpo, funcional e econômico, sem luxos desnecessários.
"""

# COZINHA ESSENTIAL
def cozinha_essential(comodo):
    return f"""
Crie uma imagem 3D fotorrealista de uma cozinha com aproximadamente {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, localizada na região {comodo['localização']} da planta.

O campo {comodo['notas']} indica os moveis, suas respectivas disposições e decoração observados na planta. Serão úteis para compor a imagem de forma mais precisa.

O cômodo deve seguir o padrão ESSENTIAL da MRV, com móveis e eletrodomésticos básicos:

- Armários de MDF branco ou amadeirado, com portas lisas e puxadores simples.
- Bancada em granito ou fórmica, na cor branca ou bege.
- Fogão 4 bocas simples, geladeira branca básica, microondas.
- Pia de inox simples com torneira convencional.
- Revestimento de azulejos brancos na parede da pia.
- Piso cerâmico claro, antiderrapante.
- Iluminação com lâmpada central e sob os armários (opcional).
- Utensílios básicos: panelas, pratos, alguns temperos, pano de prato.

O ambiente deve ser prático, limpo e funcional, adequado para o dia a dia.
"""

# VARANDA ESSENTIAL
def varanda_essential(comodo):
    return f"""
Crie uma imagem 3D fotorrealista de uma varanda com aproximadamente {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, localizada na região {comodo['localização']} da planta.

O campo {comodo['notas']} indica os moveis, suas respectivas disposições e decoração observados na planta. Serão úteis para compor a imagem de forma mais precisa.

O ambiente deve seguir o padrão ESSENTIAL da MRV, com foco em praticidade e conforto:

- Conjunto pequeno de mesa e cadeiras em fibra sintética ou alumínio em tons neutros (bege, cinza).
- Floreira ou vasos com plantas pequenas e de baixa manutenção.
- Piso cerâmico antiderrapante em tom claro.
- Guarda-corpo em alumínio e vidro temperado.
- Iluminação pontual com spot ou arandela simples.
- Cortina tipo persiana externa (opcional).
- Tapete emborrachado simples (opcional).
- Decoração minimalista com um ou dois elementos decorativos.

O ambiente deve ser acolhedor e funcional, ideal para momentos de relaxamento ao ar livre, mantendo o padrão econômico da linha Essential.
"""

# GENÉRICO ESSENTIAL
def generico_essential(comodo):
    return f"""
Crie uma imagem 3D genérica para o cômodo '{comodo['nome']}' com dimensões {comodo['dimensões']['largura']} x {comodo['dimensões']['comprimento']} cm, localizado na região {comodo['localização']} da planta.

O campo {comodo['notas']} indica os moveis, suas respectivas disposições e decoração observados na planta. Serão úteis para compor a imagem de forma mais precisa.

Decoração simples no padrão ESSENTIAL da MRV:
- Móveis funcionais em MDF branco ou amadeirado
- Cores neutras (branco, bege, cinza claro)
- Iluminação natural e artificial básica
- Acabamento econômico e prático
- Ambiente limpo e organizado
"""
