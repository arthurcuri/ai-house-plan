"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { ArrowLeft, Building2 } from "lucide-react"
import { useAuth } from "@/hooks/use-auth"
import { TokenManager } from "@/lib/token-manager"
import { CategorySelection } from "@/components/category-selection"
import { UploadSection } from "@/components/upload-section"
import { ResultSection } from "@/components/result-section"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { Avatar, AvatarFallback } from "@/components/ui/avatar"

interface AppInterfaceProps {
  onBackToLanding: () => void
}

export function AppInterface({ onBackToLanding }: AppInterfaceProps) {
  const { user, logout } = useAuth()
  const [selectedCategory, setSelectedCategory] = useState<string | null>(null)
  const [uploadedFile, setUploadedFile] = useState<File | null>(null)
  const [isGenerating, setIsGenerating] = useState(false)
  const [generatedImage, setGeneratedImage] = useState<string | null>(null)
  const [generatedImages, setGeneratedImages] = useState<any[]>([])
  const [error, setError] = useState<string | null>(null)
  const [previewData, setPreviewData] = useState<any>(null)

  const handleCategorySelect = (category: string) => {
    setSelectedCategory(category)
    // Reset previous results when category changes
    setGeneratedImage(null)
    setGeneratedImages([])
    setPreviewData(null)
    setError(null)
  }

  const handleFileUpload = (file: File) => {
    setUploadedFile(file)
    setGeneratedImage(null)
    setGeneratedImages([])
    setPreviewData(null)
    setError(null)
  }

  const handleGeneratePreview = async () => {
    if (!uploadedFile || !selectedCategory) return

    setIsGenerating(true)
    setError(null)
    setGeneratedImages([])

    try {
      const formData = new FormData()
      formData.append("floorplan", uploadedFile)
      formData.append("category", selectedCategory)

      const response = await fetch("/api/generate-preview", {
        method: "POST",
        body: formData,
      })

      if (!response.ok) {
        throw new Error("Failed to generate preview")
      }

      const jsonResponse = await response.json()
      
      console.log("Full API Response:", jsonResponse)
      
      if (jsonResponse.success) {
        // Se temos imagens geradas, mostrar o catálogo
        if (jsonResponse.data.images && jsonResponse.data.images.length > 0) {
          console.log("Found generated images:", jsonResponse.data.images.length)
          setGeneratedImages(jsonResponse.data.images)
          // Para o preview principal, usar a primeira imagem ou um placeholder
          setGeneratedImage(jsonResponse.data.images[0]?.url || "/placeholder.svg?height=400&width=600&text=Preview+Gerado")
        } else if (jsonResponse.data.interpretacao_llm) {
          // Caso seja apenas interpretação sem imagens
          console.log("Found interpretation data only")
          setPreviewData(jsonResponse.data)
          setGeneratedImage("/placeholder.svg?height=400&width=600&text=Preview+Gerado+por+IA")
        } else {
          console.log("No images or interpretation found in response")
        }
        
        console.log("Response data:", jsonResponse.data)
      } else {
        throw new Error("Invalid response format")
      }
    } catch (err) {
      setError("Falha ao gerar preview. Tente novamente.")
      console.error("Error generating preview:", err)

      // Para demonstração, mostrar um resultado placeholder após um delay
      setTimeout(() => {
        setGeneratedImage(
          `/placeholder.svg?height=400&width=600&text=Preview+${selectedCategory?.toUpperCase()}+Gerado+por+IA`,
        )
        setError(null)
      }, 2000)
    } finally {
      setIsGenerating(false)
    }
  }

  const getUserInitials = (name: string) => {
    return name
      .split(" ")
      .map((n) => n[0])
      .join("")
      .toUpperCase()
      .slice(0, 2)
  }

  const handleLogout = () => {
    logout()
    onBackToLanding()
  }

  const canGeneratePreview = selectedCategory && uploadedFile

  return (
    <div className="min-h-screen bg-white">
      {/* App Header */}
      <header className="bg-white border-b border-gray-100 shadow-sm">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-4">
              <Button variant="ghost" onClick={onBackToLanding} className="text-gray-600 hover:text-emerald-600">
                <ArrowLeft className="w-4 h-4 mr-2" />
                Voltar ao Início
              </Button>
              <div className="flex items-center gap-3">
                <div className="flex items-center gap-2">
                  <div className="w-8 h-8 bg-gradient-to-br from-emerald-500 to-emerald-600 rounded-lg flex items-center justify-center">
                    <Building2 className="w-5 h-5 text-white" />
                  </div>
                  <div className="w-8 h-8 bg-gradient-to-br from-orange-500 to-orange-600 rounded-lg flex items-center justify-center transform rotate-45">
                    <div className="w-3 h-3 bg-white rounded-sm transform -rotate-45" />
                  </div>
                </div>
                <div>
                  <h1 className="text-2xl font-bold text-gray-900">MRV AI Preview</h1>
                  <p className="text-sm text-gray-600">Selecione a categoria e faça upload da planta baixa</p>
                </div>
              </div>
            </div>

            <DropdownMenu>
              <DropdownMenuTrigger asChild>
                <Button variant="ghost" className="relative h-10 w-10 rounded-full">
                  <Avatar className="h-10 w-10">
                    <AvatarFallback className="bg-emerald-100 text-emerald-700">
                      {user?.name ? getUserInitials(user.name) : "U"}
                    </AvatarFallback>
                  </Avatar>
                </Button>
              </DropdownMenuTrigger>
              <DropdownMenuContent className="w-56" align="end" forceMount>
                <div className="flex flex-col space-y-1 p-2">
                  <p className="text-sm font-medium leading-none">{user?.name}</p>
                  <p className="text-xs leading-none text-muted-foreground">{user?.email}</p>
                </div>
                <DropdownMenuSeparator />
                <DropdownMenuItem onClick={onBackToLanding} className="cursor-pointer">
                  Voltar ao Início
                </DropdownMenuItem>
                <DropdownMenuItem className="cursor-pointer">Configurações</DropdownMenuItem>
                <DropdownMenuSeparator />
                <DropdownMenuItem onClick={handleLogout} className="cursor-pointer text-red-600">
                  Sair
                </DropdownMenuItem>
              </DropdownMenuContent>
            </DropdownMenu>
          </div>
        </div>
      </header>

      {/* App Content */}
      <main className="container mx-auto px-4 py-8 max-w-6xl space-y-12">
        {/* Category Selection */}
        <CategorySelection selectedCategory={selectedCategory} onCategorySelect={handleCategorySelect} />

        {/* Upload Section - Show when category is selected */}
        {selectedCategory && (
          <UploadSection
            onFileUpload={handleFileUpload}
            uploadedFile={uploadedFile}
            onGeneratePreview={handleGeneratePreview}
            isGenerating={isGenerating}
            disabled={!canGeneratePreview}
          />
        )}

        {/* Result Section - Show preview below upload */}
        <ResultSection 
          generatedImage={generatedImage} 
          generatedImages={generatedImages}
          isGenerating={isGenerating} 
          error={error}
          previewData={previewData}
        />
      </main>
    </div>
  )
}
