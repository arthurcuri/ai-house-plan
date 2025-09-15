# 🏠 House AI Preview - Frontend

Interface moderna e responsiva para geração de previews realistas de apartamentos a partir de plantas baixas usando Inteligência Artificial.

## 📋 Visão Geral

Este frontend oferece uma experiência completa para usuários transformarem plantas arquitetônicas em visualizações fotorrealistas. Com design moderno, autenticação segura e integração com IA, proporciona uma jornada intuitiva desde o upload da planta até a visualização dos resultados.

## 🚀 Funcionalidades

- **🏠 Landing Page Moderna**: Design responsivo com seções informativas
- **🔐 Sistema de Autenticação**: Login/registro seguro com JWT
- **📱 Interface Responsiva**: Otimizada para desktop, tablet e mobile
- **🎨 Upload Intuitivo**: Drag & drop para plantas baixas
- **🏷️ Seleção de Categorias**: Essential, Eco, Bio, Class com estilos únicos
- **🖼️ Galeria de Resultados**: Visualização organizada das imagens geradas
- **⚡ Feedback em Tempo Real**: Loading states e indicadores de progresso
- **🎯 Showcase Interativo**: Carrossel antes/depois das transformações

## 🛠️ Tecnologias

- **Framework**: Next.js 14.2.16 (React 18)
- **Linguagem**: TypeScript 5
- **Estilização**: Tailwind CSS 3.4.17
- **Componentes**: Radix UI (Headless)
- **Ícones**: Lucide React
- **Formulários**: React Hook Form + Zod
- **Autenticação**: JWT + Context API
- **Build**: Turbopack (desenvolvimento)
- **Deploy**: Docker + Standalone build

## 📁 Estrutura do Projeto

```
mrv-ai-preview-front/
├── app/                    # App Router (Next.js 14)
│   ├── layout.tsx         # Layout raiz da aplicação
│   ├── page.tsx           # Página inicial/landing
│   ├── globals.css        # Estilos globais
│   ├── login/             # Página de login
│   ├── register/          # Página de registro
│   ├── forgot-password/   # Recuperação de senha
│   └── api/               # API Routes (proxy para backend)
├── components/            # Componentes React
│   ├── ui/               # Componentes base (Radix UI)
│   ├── hero-section.tsx  # Seção principal da landing
│   ├── about-section.tsx # Sobre o produto
│   ├── preview-showcase.tsx # Carrossel antes/depois
│   ├── app-interface.tsx # Interface principal da aplicação
│   ├── category-selection.tsx # Seleção de tipos de apartamento
│   ├── upload-section.tsx # Upload de plantas
│   ├── result-section.tsx # Exibição de resultados
│   └── ...               # Outros componentes
├── hooks/                # Custom React Hooks
│   ├── use-auth.tsx      # Hook de autenticação
│   ├── useImageGeneration.ts # Hook para geração de imagens
│   └── use-toast.ts      # Hook para notificações
├── lib/                  # Utilitários
│   ├── config.ts         # Configurações da API
│   ├── images.ts         # Configuração de imagens
│   ├── token-manager.ts  # Gerenciamento de tokens JWT
│   └── utils.ts          # Utilitários gerais
├── public/               # Arquivos estáticos
│   └── images/           # Imagens do site
│       ├── hero/         # Imagem principal
│       └── showcase/     # Imagens antes/depois
├── styles/               # Estilos adicionais
└── Docker & Config files # Configurações de deploy
```

## ⚙️ Configuração e Instalação

### Pré-requisitos

- Node.js 18+ 
- pnpm (recomendado) ou npm
- Backend do House AI Preview rodando
- Docker (opcional)

### 1. Instalação Local

```bash
# Clonar o repositório
git clone <seu-repositorio>
cd mrv-ai-preview-front

# Instalar dependências
pnpm install
# ou
npm install

# Configurar variáveis de ambiente
cp .env.local.example .env.local
```

### 2. Configuração do Ambiente

Edite o `.env.local`:
```env
# URL do Backend
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000

# Configurações de Desenvolvimento
NODE_ENV=development
NEXT_PUBLIC_APP_NAME="House AI Preview"
NEXT_PUBLIC_APP_VERSION="1.0.0"

# Analytics (opcional)
NEXT_PUBLIC_GA_ID=your_google_analytics_id
```

### 3. Executar em Desenvolvimento

```bash
# Modo desenvolvimento
pnpm dev
# ou
npm run dev

# A aplicação estará disponível em:
# http://localhost:3000
```

### 4. Build para Produção

```bash
# Build otimizado
pnpm build
pnpm start

# Ou com npm
npm run build
npm start
```

## 🐳 Deploy com Docker

### 1. Usando Docker Compose (Recomendado)

```bash
# Build e deploy completo
docker-compose up --build -d

# Ver logs
docker-compose logs -f frontend
```

### 2. Docker Manual

```bash
# Build da imagem
docker build -t house-ai-frontend .

# Executar container
docker run -d \
  --name house-ai-frontend \
  -p 3000:3000 \
  -e NEXT_PUBLIC_API_URL=http://backend:8000 \
  house-ai-frontend
```

## 🎨 Componentes Principais

### Landing Page

- **🏠 Hero Section**: Apresentação principal com CTA
- **📖 About Section**: Benefícios e funcionalidades
- **⚙️ How It Works**: Processo em 3 passos
- **🖼️ Preview Showcase**: Carrossel interativo antes/depois
- **❓ FAQ Section**: Perguntas frequentes
- **📞 Footer**: Contato e links úteis

### App Interface

- **🏷️ Category Selection**: 4 tipos de apartamento
  - **Essential**: Moderno e funcional
  - **Eco**: Sustentável com tecnologia verde
  - **Bio**: Natural com materiais orgânicos
  - **Class**: Luxuoso com acabamentos premium

- **📤 Upload Section**: 
  - Drag & drop interface
  - Validação de arquivo (jpg, png, pdf)
  - Preview da imagem enviada

- **🖼️ Result Section**:
  - Galeria de imagens geradas
  - Download individual ou em lote
  - Organização por cômodos

## 🎨 Sistema de Design

### Cores Principais
```css
/* Emerald (Principal) */
--emerald-50: #ecfdf5;
--emerald-500: #10b981;
--emerald-600: #059669;

/* Orange (Secundária) */
--orange-50: #fff7ed;
--orange-500: #f97316;
--orange-600: #ea580c;

/* Grays (Neutros) */
--gray-50: #f9fafb;
--gray-900: #111827;
```

### Tipografia
- **Font**: Inter (Google Fonts)
- **Heading**: Font-bold, sizes 2xl-6xl
- **Body**: Font-normal, sizes sm-xl
- **Captions**: Font-medium, size xs-sm

### Componentes UI
Baseados no **Radix UI** para acessibilidade:
- Buttons com variants (default, outline, ghost)
- Cards com shadow e hover effects
- Modals e dialogs acessíveis
- Form controls com validação visual

## 🔐 Autenticação

### Fluxo de Autenticação
1. **Login/Registro**: Formulários com validação
2. **JWT Storage**: Tokens armazenados com segurança
3. **Auto-refresh**: Renovação automática de tokens
4. **Protected Routes**: Acesso controlado à app interface

### Hooks de Autenticação
```typescript
const { user, isAuthenticated, login, logout } = useAuth()

// Verificar se usuário está logado
if (isAuthenticated) {
  // Mostrar interface da aplicação
}
```

## 📱 Responsividade

### Breakpoints
- **Mobile**: 0-768px
- **Tablet**: 768px-1024px  
- **Desktop**: 1024px+

### Layout Adaptativo
- **Mobile**: Stack vertical, menu hamburger
- **Tablet**: Grid 2 colunas, sidebar compacta
- **Desktop**: Grid 3+ colunas, sidebar completa

## 🖼️ Sistema de Imagens

### Estrutura de Imagens
```
public/images/
├── hero/
│   └── main-hero.jpg          # Imagem principal (800x600)
└── showcase/
    ├── before/                # Plantas baixas
    │   ├── before-1.png       # (400x300)
    │   ├── before-2.png
    │   └── before-3.jpg
    └── after/                 # Previews IA
        ├── after-1.png        # (400x300)
        ├── after-2.png
        └── after-3.png
```

### Otimização
- **Next.js Image**: Otimização automática
- **Lazy Loading**: Carregamento sob demanda
- **WebP Support**: Formatos modernos quando suportados
- **Responsive Images**: Múltiplas resoluções

## 🚀 Performance

### Otimizações Implementadas
- **Code Splitting**: Carregamento por rotas
- **Tree Shaking**: Remoção de código não usado
- **Bundle Analysis**: Monitoramento do tamanho
- **Edge Runtime**: API routes otimizadas
- **Static Generation**: Páginas estáticas quando possível

### Métricas Alvo
- **First Contentful Paint**: < 1.5s
- **Largest Contentful Paint**: < 2.5s
- **Cumulative Layout Shift**: < 0.1
- **Time to Interactive**: < 3s

## 🧪 Desenvolvimento

### Scripts Disponíveis
```bash
# Desenvolvimento
pnpm dev              # Servidor de desenvolvimento
pnpm build           # Build de produção
pnpm start           # Servidor de produção
pnpm lint            # Linting com ESLint

# Utilitários
pnpm type-check      # Verificação de tipos TypeScript
pnpm analyze         # Análise do bundle
```

### Estrutura de Componentes
```typescript
// Exemplo de componente
interface ComponentProps {
  title: string
  onAction: () => void
}

export function Component({ title, onAction }: ComponentProps) {
  return (
    <div className="p-4 rounded-lg bg-white shadow">
      <h2 className="text-xl font-bold">{title}</h2>
      <Button onClick={onAction}>Ação</Button>
    </div>
  )
}
```

## 🔧 Configurações Avançadas

### Next.js Config
```javascript
// next.config.mjs
const nextConfig = {
  output: 'standalone',           // Para Docker
  images: { unoptimized: true },  // Compatibilidade
  experimental: {
    turbo: true                   // Turbopack no dev
  }
}
```

### Tailwind Config
```javascript
// tailwind.config.ts
module.exports = {
  content: ['./app/**/*.tsx', './components/**/*.tsx'],
  theme: {
    extend: {
      colors: {
        emerald: { /* cores customizadas */ },
        orange: { /* cores customizadas */ }
      }
    }
  }
}
```

## 🐛 Troubleshooting

### Problemas Comuns

1. **Erro de conexão com backend**
   ```bash
   # Verificar se backend está rodando
   curl http://127.0.0.1:8000/docs
   
   # Verificar variável de ambiente
   echo $NEXT_PUBLIC_API_URL
   ```

2. **Erro de build**
   ```bash
   # Limpar cache
   rm -rf .next
   pnpm build
   ```

3. **Problemas de autenticação**
   ```bash
   # Verificar localStorage
   # Developer Tools > Application > Local Storage
   ```

### Debug Mode
```bash
# Ativar logs detalhados
DEBUG=* pnpm dev

# Ou apenas Next.js
DEBUG=next:* pnpm dev
```

## 📊 Monitoramento

### Analytics
- **Google Analytics**: Configurado via GA_ID
- **Performance Monitoring**: Web Vitals integrados
- **Error Tracking**: Sentry (configuração opcional)

### Logs
```typescript
// utils/logger.ts
export const logger = {
  info: (message: string) => console.log(`[INFO] ${message}`),
  error: (message: string) => console.error(`[ERROR] ${message}`)
}
```

## 🚀 Deploy em Produção

### Checklist de Deploy
- [ ] Configurar variáveis de ambiente de produção
- [ ] Configurar domínio e SSL
- [ ] Configurar CDN para assets estáticos
- [ ] Implementar monitoramento
- [ ] Configurar backup automático
- [ ] Testar em diferentes dispositivos

### Variáveis de Produção
```env
NODE_ENV=production
NEXT_PUBLIC_API_URL=https://api.houseai.com
NEXT_PUBLIC_CDN_URL=https://cdn.houseai.com
```

### Nginx Proxy (Produção)
```nginx
server {
    listen 80;
    server_name houseai.com;
    
    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
    
    location /_next/static/ {
        alias /app/.next/static/;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

## 📞 Suporte

- **Email**: arthur1curi@gmail.com
- **WhatsApp**: +55 (31) 9341-6474
- **Localização**: Belo Horizonte, MG, Brasil

## 📄 Licença

Este projeto é propriedade privada. Todos os direitos reservados.

---

## 🛣️ Roadmap

### Próximas Funcionalidades
- [ ] 🎨 Editor de materiais e acabamentos
- [ ] 🔄 Histórico de gerações
- [ ] 📱 Progressive Web App (PWA)
- [ ] 🌙 Dark mode
- [ ] 🌍 Internacionalização (i18n)
- [ ] 📊 Dashboard de analytics
- [ ] 🔗 Compartilhamento social
- [ ] 💳 Sistema de pagamento

### Melhorias Técnicas
- [ ] ⚡ Server Components migration
- [ ] 🧪 Testes automatizados (Jest + Testing Library)
- [ ] 📈 Bundle size optimization
- [ ] 🔍 SEO improvements
- [ ] ♿ Accessibility audit (WCAG 2.1)

---

**House AI Preview Frontend** - Transformando a experiência de visualização imobiliária com tecnologia de ponta 🏠✨