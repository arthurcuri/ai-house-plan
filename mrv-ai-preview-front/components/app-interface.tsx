"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { ArrowLeft, Building2 } from "lucide-react"
import { useAuth } from "@/hooks/use-auth"
import { UploadSection } from "@/components/upload-section"
import { ResultSection } from "@/components/result-section"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"

interface AppInterfaceProps {
  onBackToLanding: () => void
}

export function AppInterface({ onBackToLanding }: AppInterfaceProps) {
  const { user, logout } = useAuth()
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
      formData.append("floorplan", uploadedFile) // Mudança: volta para "floorplan" para corresponder à API route

      const response = await fetch("/api/generate-preview", {
        // Usar a rota da API do Next.js
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
      setError("Falha ao gerar preview. Tente novamente.")
      console.error("Error generating preview:", err)

      // Para demonstração, mostrar um resultado placeholder após um delay
      setTimeout(() => {
        setGeneratedImage("/placeholder.svg?height=400&width=600&text=Preview+Gerado+por+IA")
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

  return (
    <div className="min-h-screen bg-white">
      {/* App Header */}
      <header className="bg-white border-b border-gray-100 shadow-sm">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-4">
              <Button variant="ghost" onClick={onBackToLanding} className="text-gray-600 hover:text-emerald-600">
                <ArrowLeft className="w-4 h-4 mr-2" />
                Back to Landing
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
                  <p className="text-sm text-gray-600">
                    Upload a floor plan and generate a realistic apartment preview
                  </p>
                </div>
              </div>
            </div>

            <DropdownMenu>
              <DropdownMenuTrigger asChild>
                <Button variant="ghost" className="relative h-10 w-10 rounded-full">
                  <Avatar className="h-10 w-10">
                    <AvatarImage src={user?.avatar || "/placeholder.svg"} alt={user?.name} />
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
                  Back to Landing
                </DropdownMenuItem>
                <DropdownMenuItem className="cursor-pointer">Settings</DropdownMenuItem>
                <DropdownMenuSeparator />
                <DropdownMenuItem onClick={handleLogout} className="cursor-pointer text-red-600">
                  Log out
                </DropdownMenuItem>
              </DropdownMenuContent>
            </DropdownMenu>
          </div>
        </div>
      </header>

      {/* App Content */}
      <main className="container mx-auto px-4 py-8 max-w-4xl">
        <UploadSection
          onFileUpload={handleFileUpload}
          uploadedFile={uploadedFile}
          onGeneratePreview={handleGeneratePreview}
          isGenerating={isGenerating}
          disabled={!uploadedFile}
        />

        <ResultSection generatedImage={generatedImage} isGenerating={isGenerating} error={error} />
      </main>
    </div>
  )
}
