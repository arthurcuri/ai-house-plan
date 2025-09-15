"use client"

import { useState } from 'react'

interface GeneratedImage {
  id: number
  name: string
  url: string
  description: string
  room: string
  category: string
}

export function useImageGeneration() {
  const [images, setImages] = useState<GeneratedImage[]>([])
  const [isGenerating, setIsGenerating] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [showGallery, setShowGallery] = useState(false)

  const generateImages = async (file: File, category: string) => {
    setIsGenerating(true)
    setError(null)
    setShowGallery(true)
    setImages([])

    try {
      const formData = new FormData()
      formData.append('floorplan', file)
      formData.append('category', category)

      console.log('Enviando requisição para gerar imagens...')

      const response = await fetch('/api/generate-preview', {
        method: 'POST',
        body: formData,
      })

      const result = await response.json()

      if (!response.ok) {
        throw new Error(result.error || `Erro ${response.status}: ${result.details || 'Erro desconhecido'}`)
      }

      if (result.success && result.data.images && result.data.images.length > 0) {
        setImages(result.data.images)
        console.log(`${result.data.images.length} imagens geradas com sucesso`)
      } else {
        throw new Error(result.data?.metadata?.message || 'Nenhuma imagem foi gerada')
      }

    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Erro desconhecido'
      setError(errorMessage)
      console.error('Erro na geração de imagens:', err)
    } finally {
      setIsGenerating(false)
    }
  }

  const closeGallery = () => {
    setShowGallery(false)
    setImages([])
    setError(null)
    setIsGenerating(false)
  }

  return {
    images,
    isGenerating,
    error,
    showGallery,
    generateImages,
    closeGallery
  }
}
