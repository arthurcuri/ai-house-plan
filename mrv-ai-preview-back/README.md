# 🏠 House AI Preview - Backend

API Backend para geração de previews realistas de apartamentos a partir de plantas baixas usando Inteligência Artificial.

## 📋 Visão Geral

Este backend processa plantas arquitetônicas, extrai informações dos cômodos via OCR e gera visualizações fotorrealistas usando Google Gemini AI. O sistema suporta diferentes categorias de apartamentos (Essential, Eco, Bio, Class) com estilos específicos para cada uma.

## 🚀 Funcionalidades

- **🔍 OCR Inteligente**: Extração de texto de plantas baixas usando EasyOCR
- **🤖 Interpretação IA**: Análise de plantas via Google Gemini para identificar cômodos
- **🎨 Geração de Imagens**: Criação de previews fotorrealistas em alta definição
- **👥 Sistema de Autenticação**: Login/registro com JWT
- **📁 Gestão de Arquivos**: Organização automática de imagens geradas
- **🏷️ Categorias de Apartamentos**: Essential, Eco, Bio, Class com estilos únicos

## 🛠️ Tecnologias

- **Framework**: FastAPI (Python 3.12+)
- **IA**: Google Gemini AI
- **OCR**: EasyOCR
- **Autenticação**: JWT + SQLAlchemy
- **Banco de Dados**: SQLite (desenvolvimento)
- **Processamento de Imagens**: Pillow
- **Deploy**: Docker + Uvicorn

## 📁 Estrutura do Projeto

```
mrv-ai-preview-back/
├── main.py                 # Entrada principal da aplicação
├── pyproject.toml         # Dependências e configuração
├── Dockerfile             # Container Docker
├── auth.db               # Banco de dados SQLite
├── generated_images/     # Imagens geradas organizadas por sessão
│   └── YYYYMMDD_HHMMSS_sessionid/
│       ├── comodo_1_sala.png
│       ├── comodo_2_quarto.png
│       └── ...
└── utils/
    ├── api/              # API Routes e configuração
    │   ├── main.py      # Configuração principal da API
    │   └── routes/      # Endpoints organizados
    │       ├── image_generation.py  # Geração de imagens
    │       └── ocr.py   # Processamento OCR
    ├── auth/            # Sistema de autenticação
    ├── core/            # Lógica de negócio
    │   ├── ai/          # Integração com Gemini AI
    │   ├── image_generation/  # Geração de imagens
    │   └── ocr/         # Processamento OCR
    ├── database/        # Modelos e serviços de BD
    └── shared/          # Utilidades compartilhadas
```

## ⚙️ Configuração e Instalação

### Pré-requisitos

- Python 3.12+
- UV (gerenciador de dependências)
- Google Gemini API Key
- Docker (opcional)

### 1. Instalação com UV

```bash
# Clonar o repositório
git clone <seu-repositorio>
cd mrv-ai-preview-back

# Instalar dependências
uv sync

# Ativar ambiente virtual
source .venv/bin/activate  # Linux/Mac
# ou
.venv\\Scripts\\activate   # Windows
```

### 2. Configuração das Variáveis de Ambiente

```bash
# Criar arquivo .env na raiz
cp .env.example .env
```

Edite o `.env` com suas configurações:
```env
# Google Gemini AI
GOOGLE_API_KEY=sua_api_key_aqui

# JWT
SECRET_KEY=sua_chave_secreta_jwt
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Banco de Dados
DATABASE_URL=sqlite:///./auth.db

# Configurações da API
HOST=127.0.0.1
PORT=8000
DEBUG=True
```

### 3. Inicializar Banco de Dados

```bash
python init_db.py
```

### 4. Executar a Aplicação

```bash
# Desenvolvimento
python main.py

# Ou com uvicorn diretamente
uvicorn utils.api.main:app --host 127.0.0.1 --port 8000 --reload
```

A API estará disponível em: `http://127.0.0.1:8000`

## 🐳 Deploy com Docker

### 1. Criar Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \\
    libgl1-mesa-glx \\
    libglib2.0-0 \\
    libsm6 \\
    libxext6 \\
    libxrender-dev \\
    libgomp1 \\
    libgfortran5 \\
    && rm -rf /var/lib/apt/lists/*

# Copiar arquivos de dependências
COPY pyproject.toml uv.lock ./

# Instalar UV e dependências
RUN pip install uv
RUN uv sync --frozen

# Copiar código fonte
COPY . .

# Criar diretórios necessários
RUN mkdir -p generated_images

# Expor porta
EXPOSE 8000

# Comando para iniciar
CMD ["uv", "run", "uvicorn", "utils.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 2. Build e Run

```bash
# Build da imagem
docker build -t house-ai-backend .

# Executar container
docker run -d \\
  --name house-ai-backend \\
  -p 8000:8000 \\
  -v $(pwd)/generated_images:/app/generated_images \\
  -v $(pwd)/.env:/app/.env \\
  house-ai-backend
```

## 📚 Endpoints da API

### 🔐 Autenticação

```bash
# Registrar usuário
POST /auth/register
Content-Type: application/json
{
  "email": "user@example.com",
  "password": "senha123"
}

# Login
POST /auth/login
Content-Type: application/x-www-form-urlencoded
username=user@example.com&password=senha123
```

### 🖼️ Processamento de Imagens

```bash
# Gerar previews de apartamento
POST /gerar-imagens
Content-Type: multipart/form-data
- file: <arquivo_planta_baixa.jpg>
- tipo: "essential|eco|bio|class"
```

**Resposta:**
```json
{
  "modo": "arquivos_hd",
  "tipo": "ESSENTIAL",
  "quantidade_comodos": 5,
  "session_id": "20240914_203708_10300cc8",
  "resultado": [
    {
      "comodo": "Sala de Estar",
      "prompt": "...",
      "url_relativa": "/imagens/20240914_203708_10300cc8/comodo_1_sala_estar.png",
      "tamanho_bytes": 2048576,
      "dimensoes": {"largura": "4.5m", "altura": "3.2m"}
    }
  ]
}
```

### 📱 OCR

```bash
# Extrair texto de planta baixa
POST /ocr
Content-Type: multipart/form-data
- file: <arquivo_planta_baixa.jpg>
```

## 🏷️ Categorias de Apartamentos

### Essential
- **Estilo**: Moderno e funcional
- **Características**: Acabamentos de qualidade, design clean
- **Público**: Primeira habitação, jovens profissionais

### Eco
- **Estilo**: Sustentável e tecnológico
- **Características**: Painéis solares, materiais ecológicos
- **Público**: Ambientalmente conscientes

### Bio
- **Estilo**: Natural e orgânico
- **Características**: Materiais naturais, plantas integradas
- **Público**: Amantes da natureza

### Class
- **Estilo**: Luxuoso e premium
- **Características**: Acabamentos nobres, móveis de grife
- **Público**: Alto padrão

## 🔧 Configurações Avançadas

### Qualidade das Imagens

As imagens são geradas em ultra alta qualidade:
- **Formato**: PNG sem compressão
- **Rendering**: Fotorrealístico com ray tracing
- **Resolução**: Máxima disponível no modelo
- **Anti-aliasing**: Ativado

### Performance

```python
# Configurações em utils/core/ai/gemini_service.py
CONFIGURACAO = {
    "max_tentativas": 8,
    "delay_progressivo": "5s até 80s",
    "timeout": 120,
    "qualidade": "ULTRA_HD"
}
```

## 📊 Monitoramento

### Logs da Aplicação

```bash
# Ver logs em tempo real
docker logs -f house-ai-backend

# Logs de acesso
tail -f logs/access.log
```

### Métricas

- Tempo médio de processamento: ~30-60s por cômodo
- Taxa de sucesso OCR: ~95%
- Qualidade das imagens: Ultra HD (2-5MB por imagem)

## 🧪 Testes

```bash
# Executar testes
python test_api.py

# Teste manual da API
curl -X POST "http://127.0.0.1:8000/gerar-imagens" \\
  -H "Content-Type: multipart/form-data" \\
  -F "file=@planta_exemplo.jpg" \\
  -F "tipo=essential"
```

## 🚀 Deploy em Produção

### Checklist de Deploy

- [ ] Configurar variáveis de ambiente de produção
- [ ] Configurar proxy reverso (Nginx)
- [ ] Implementar HTTPS
- [ ] Configurar backup automático das imagens
- [ ] Monitoramento com logs estruturados
- [ ] Rate limiting para APIs externas

### Nginx Configuration

```nginx
server {
    listen 80;
    server_name api.houseai.com;
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
    
    location /imagens/ {
        alias /app/generated_images/;
        expires 7d;
        add_header Cache-Control "public, immutable";
    }
}
```

## 🐛 Troubleshooting

### Problemas Comuns

1. **Erro de API Key**: Verificar se `GOOGLE_API_KEY` está configurada
2. **OCR falha**: Verificar qualidade/resolução da imagem de entrada
3. **Timeout na geração**: Aumentar timeout nas configurações
4. **Erro de dependências**: Rodar `uv sync` novamente

### Logs de Debug

```bash
# Ativar logs detalhados
export LOG_LEVEL=DEBUG
python main.py
```

## 📞 Suporte

- **Email**: arthur1curi@gmail.com
- **WhatsApp**: +55 (31) 9341-6474
- **Localização**: Belo Horizonte, MG, Brasil

## 📄 Licença

Este projeto é propriedade privada. Todos os direitos reservados.

---

**House AI Preview Backend** - Transformando plantas baixas em realidade virtual desde 2024 🏠✨