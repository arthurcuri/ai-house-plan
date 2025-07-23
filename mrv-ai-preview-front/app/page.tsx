"use client"

import { useState } from "react"
import { Header } from "@/components/header"
import { UploadSection } from "@/components/upload-section"
import { HeroSection } from "@/components/hero-section"
import { AboutSection } from "@/components/about-section"
import { HowItWorksSection } from "@/components/how-it-works-section"
import { PreviewShowcase } from "@/components/preview-showcase"
import { FAQSection } from "@/components/faq-section"
import { Footer } from "@/components/footer"

export default function LandingPage() {
  const [uploadedFile, setUploadedFile] = useState<File | null>(null)
  const [isGenerating, setIsGenerating] = useState(false)
  const [generatedImage, setGeneratedImage] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)

  const handleFileUpload = (file: File) => {
    setUploadedFile(file)
    setGeneratedImage(null)
    setError(null)
  }

  const handleGeneratePreview = async () => {
    if (!uploadedFile) return

    setIsGenerating(true)
    setError(null)

    try {
      const formData = new FormData()
      formData.append("floorplan", uploadedFile)

      // This would be the actual API call to your Python backend
      const response = await fetch("/api/generate-preview", {
        method: "POST",
        body: formData,
      })

      if (!response.ok) {
        throw new Error("Failed to generate preview")
      }

      const blob = await response.blob()
      const imageUrl = URL.createObjectURL(blob)
      setGeneratedImage(imageUrl)
    } catch (err) {
      setError("Failed to generate preview. Please try again.")
      console.error("Error generating preview:", err)

      // For demo purposes, show a placeholder result after a delay
      setTimeout(() => {
        setGeneratedImage("/placeholder.svg?height=400&width=600")
        setError(null)
      }, 2000)
    } finally {
      setIsGenerating(false)
    }
  }

  return (
    <div className="min-h-screen bg-white">
      <Header />
      <main>
        <HeroSection />
        <AboutSection />
        <HowItWorksSection />
        <UploadSection
          onFileUpload={handleFileUpload}
          uploadedFile={uploadedFile}
          onGeneratePreview={handleGeneratePreview}
          isGenerating={isGenerating}
          disabled={!uploadedFile}
        />
        <PreviewShowcase generatedImage={generatedImage} isGenerating={isGenerating} error={error} />
        <FAQSection />
      </main>
      <Footer />
    </div>
  )
}
