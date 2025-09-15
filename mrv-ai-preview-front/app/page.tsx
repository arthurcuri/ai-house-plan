"use client"

import React, { useState, useEffect } from 'react'
import { useAuth } from "@/hooks/use-auth"
import { useSearchParams } from "next/navigation"
import { Header } from "@/components/header"
import { HeroSection } from "@/components/hero-section"
import { AboutSection } from "@/components/about-section"
import { HowItWorksSection } from "@/components/how-it-works-section"
import { PreviewShowcase } from "@/components/preview-showcase"
import { FAQSection } from "@/components/faq-section"
import { Footer } from "@/components/footer"
import { AppInterface } from "@/components/app-interface"
import { useImageGeneration } from '@/hooks/useImageGeneration'
import ImageGallery from '@/components/ImageGallery'

export default function Home() {
  const { user, isAuthenticated, isLoading } = useAuth()
  const [showApp, setShowApp] = useState(false)
  const [selectedFile, setSelectedFile] = useState<File | null>(null)
  const [selectedCategory, setSelectedCategory] = useState<string>('')
  const searchParams = useSearchParams()

  const { 
    images, 
    isGenerating, 
    error, 
    showGallery, 
    generateImages, 
    closeGallery 
  } = useImageGeneration()

  // Verificar se deve iniciar o app automaticamente após login
  useEffect(() => {
    const startApp = searchParams.get('start-app')
    if (startApp === 'true' && isAuthenticated && !isLoading) {
      setShowApp(true)
    }
  }, [isAuthenticated, isLoading, searchParams])

  const handleTryNow = () => {
    if (isLoading) {
      return // Evitar ação durante carregamento
    }
    
    if (isAuthenticated) {
      setShowApp(true)
    } else {
      // Redirect to login page com parâmetro para voltar à aplicação
      const currentUrl = window.location.href
      window.location.href = `/login?redirect=${encodeURIComponent(currentUrl)}&action=start-app`
    }
  }

  const handleFileSelect = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0]
    if (file) {
      setSelectedFile(file)
    }
  }

  const handleGeneratePreview = async () => {
    if (!selectedFile) {
      alert('Por favor, selecione uma imagem da planta')
      return
    }
    
    if (!selectedCategory) {
      alert('Por favor, selecione uma categoria')
      return
    }

    await generateImages(selectedFile, selectedCategory)
  }

  if (showApp && isAuthenticated) {
    return <AppInterface onBackToLanding={() => setShowApp(false)} />
  }

  return (
    <div className="min-h-screen bg-white">
      <Header onTryNow={handleTryNow} />
      <main>
        <HeroSection onTryNow={handleTryNow} />
        <AboutSection />
        <HowItWorksSection />
        <PreviewShowcase />
        <FAQSection />
      </main>
      <Footer />
      <main className="container mx-auto p-6 max-w-4xl">
        <h1 className="text-3xl font-bold text-center mb-8">MRV AI Preview</h1>
        
        <div className="bg-white rounded-lg shadow-lg p-6 space-y-6">
          {/* Upload de arquivo */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Planta Arquitetônica
            </label>
            <input
              type="file"
              accept="image/*"
              onChange={handleFileSelect}
              className="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
            />
          </div>

          {/* Seleção de categoria */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Categoria
            </label>
            <select
              value={selectedCategory}
              onChange={(e) => setSelectedCategory(e.target.value)}
              className="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            >
              <option value="">Selecione uma categoria</option>
              <option value="eco">Eco</option>
              <option value="essential">Essential</option>
              <option value="bio">Bio</option>
              <option value="class">Class</option>
            </select>
          </div>

          {/* Botão de gerar */}
          <button
            onClick={handleGeneratePreview}
            disabled={!selectedFile || !selectedCategory || isGenerating}
            className="w-full bg-blue-600 text-white py-3 px-4 rounded-md hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed font-medium"
          >
            {isGenerating ? 'Gerando Imagens...' : 'Gerar Preview'}
          </button>

          {/* Mostrar erro se houver */}
          {error && (
            <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded">
              <strong>Erro:</strong> {error}
            </div>
          )}
        </div>

        {/* Galeria de imagens */}
        {showGallery && (
          <ImageGallery
            images={images}
            category={selectedCategory}
            onClose={closeGallery}
            isLoading={isGenerating}
          />
        )}
      </main>
    </div>
  )
}
