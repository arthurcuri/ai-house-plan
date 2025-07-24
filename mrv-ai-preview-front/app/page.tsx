"use client"

import { useState } from "react"
import { useAuth } from "@/hooks/use-auth"
import { Header } from "@/components/header"
import { HeroSection } from "@/components/hero-section"
import { AboutSection } from "@/components/about-section"
import { HowItWorksSection } from "@/components/how-it-works-section"
import { PreviewShowcase } from "@/components/preview-showcase"
import { FAQSection } from "@/components/faq-section"
import { Footer } from "@/components/footer"
import { AppInterface } from "@/components/app-interface"

export default function Home() {
  const { user, isAuthenticated } = useAuth()
  const [showApp, setShowApp] = useState(false)

  const handleTryNow = () => {
    if (isAuthenticated) {
      setShowApp(true)
    } else {
      // Redirect to login page
      window.location.href = "/login"
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
