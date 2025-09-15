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

export default function Home() {
  const { user, isAuthenticated, isLoading } = useAuth()
  const [showApp, setShowApp] = useState(false)
  const searchParams = useSearchParams()

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
    </div>
  )
}
