# utils/core/ai/schemas.py

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class Dimensoes(BaseModel):
    """Dimensões do cômodo em centímetros e metros"""
    largura_cm: float = Field(description="Largura do cômodo em centímetros")
    comprimento_cm: float = Field(description="Comprimento do cômodo em centímetros")
    largura_m: float = Field(description="Largura do cômodo em metros (calculado)")
    comprimento_m: float = Field(description="Comprimento do cômodo em metros (calculado)")

class PosicionamentoMovel(BaseModel):
    """Posicionamento detalhado de um móvel"""
    dimensoes: str = Field(description="Dimensões do móvel (ex: '2.2m x 0.9m')")
    posicao: str = Field(description="Posição do móvel (ex: 'contra parede norte, centralizado')")
    distancia_paredes: Optional[str] = Field(None, description="Distâncias das paredes em cm")

class PosicionamentoMoveis(BaseModel):
    """Container para posicionamento de múltiplos móveis"""
    sofa: Optional[PosicionamentoMovel] = None
    tv: Optional[PosicionamentoMovel] = None
    mesa: Optional[PosicionamentoMovel] = None
    cama: Optional[PosicionamentoMovel] = None
    armario: Optional[PosicionamentoMovel] = None
    # Adicionar outros móveis conforme necessário

class Comodo(BaseModel):
    """Estrutura completa de um cômodo"""
    nome: str = Field(description="Nome do cômodo em português")
    tipo: str = Field(
        description="Tipo do cômodo: quarto_pequeno, quarto_casal, sala, sala_cozinha, banheiro, cozinha, lavanderia, escritorio, closet, suite, varanda, area_privativa, corredor, hall, sacada, area_gourmet, home_office, outro",
        pattern="^(quarto_pequeno|quarto_casal|sala|sala_cozinha|banheiro|cozinha|lavanderia|escritorio|closet|suite|varanda|area_privativa|corredor|hall|sacada|area_gourmet|home_office|outro)$"
    )
    dimensoes: Dimensoes = Field(description="Dimensões do cômodo")
    area_m2: float = Field(description="Área do cômodo em metros quadrados")
    proporcao: str = Field(description="Forma/proporção: retangular alongado, quadrado, retangular estreito, L-shaped, etc.")
    localizacao: str = Field(description="Localização relativa: upper left, center, north, south, etc.")
    escala_relativa: Optional[str] = Field(None, description="Contexto de escala: maior cômodo, menor cômodo, cômodo médio")
    elementos_fixos: List[str] = Field(default_factory=list, description="Elementos fixos: janelas, portas, colunas com posições")
    sugestao_layout: Optional[str] = Field(None, description="Sugestão de layout baseada nas dimensões")
    posicionamento_moveis: Optional[PosicionamentoMoveis] = Field(None, description="Posicionamento detalhado dos móveis")
    notas: str = Field(description="Observações detalhadas em inglês sobre layout, mobiliário, escala e posicionamento")

class ContextoGeral(BaseModel):
    """Contexto geral do apartamento"""
    tipo_apartamento: str = Field(description="Tipo do apartamento: essential, eco, bio, class")
    orientacao_solar: Optional[str] = Field(None, description="Orientação solar: north, south, east, west")
    fluxo_circulacao: Optional[str] = Field(None, description="Fluxo de circulação: linear, circular, etc.")
    area_total_estimada_m2: Optional[float] = Field(None, description="Área total estimada do apartamento em m²")

class InterpretacaoPlanta(BaseModel):
    """Estrutura completa da interpretação da planta"""
    comodos: List[Comodo] = Field(description="Lista de cômodos identificados")
    contexto_geral: Optional[ContextoGeral] = Field(None, description="Contexto geral do apartamento")

class AnaliseEstiloArquitetura(BaseModel):
    """Schema para análise de estilo arquitetônico e geração de prompts"""
    analise_estilo: str = Field(
        description="Descrição detalhada do estilo arquitetônico identificado nas fotos, incluindo cores, materiais, mobiliário, iluminação e elementos decorativos característicos"
    )
    prompts: Dict[str, str] = Field(
        description="Dicionário com prompts personalizados para cada tipo de cômodo. Chaves: quarto_pequeno, quarto_casal, suite, sala, sala_cozinha, cozinha, banheiro, varanda, sacada, lavanderia, escritorio, home_office, closet, corredor, hall, area_privativa, area_gourmet, generico"
    )