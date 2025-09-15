// Image configuration for easy replacement
// Replace the image files in the corresponding folders with the same names

export const images = {
  // Main hero image
  hero: {
    main: '/images/hero/main-hero.jpg',
    alt: 'Preview de apartamento gerado por IA - Casa moderna e elegante'
  },

  // Category images (optional - can be placeholder for now)
  categories: {
    class: '/images/categories/class.jpg',
    bio: '/images/categories/bio.jpg', 
    eco: '/images/categories/eco.jpg',
    essential: '/images/categories/essential.jpg'
  },

  // Showcase before/after images
  showcase: {
    before: [
      {
        src: '/images/showcase/before/before-1.jpg',
        alt: 'Planta baixa 1 - Apartamento Studio'
      },
      {
        src: '/images/showcase/before/before-2.png', 
        alt: 'Planta baixa 2 - Apartamento 2 quartos'
      },
      {
        src: '/images/showcase/before/before-3.jpg',
        alt: 'Planta baixa 3 - Cobertura de luxo'
      }
    ],
    after: [
      {
        src: '/images/showcase/after/after-1.png',
        alt: 'Preview IA 1 - Studio moderno renderizado'
      },
      {
        src: '/images/showcase/after/after-2.png',
        alt: 'Preview IA 2 - Apartamento 2 quartos renderizado'  
      },
      {
        src: '/images/showcase/after/after-3.png',
        alt: 'Preview IA 3 - Cobertura de luxo renderizada'
      }
    ]
  }
}

// Showcase items configuration
export const showcaseItems = [
  {
    title: "Apartamento Studio Moderno",
    description: "Convertido de uma planta baixa simples para uma visualização 3D impressionante"
  },
  {
    title: "Layout de Dois Quartos", 
    description: "Completo com disposição de móveis e iluminação realista"
  },
  {
    title: "Cobertura de Luxo",
    description: "Visualização de acabamentos premium e materiais de alta qualidade"
  }
]

// Helper function to get image with fallback
export function getImageSrc(imagePath: string, fallback?: string): string {
  return imagePath || fallback || '/placeholder.svg?height=300&width=400&text=Imagem+Não+Encontrada'
}