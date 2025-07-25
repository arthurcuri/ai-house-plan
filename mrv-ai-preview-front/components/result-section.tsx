"use client"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Download, Eye, X } from "lucide-react"
import Image from "next/image"

interface ResultSectionProps {
  generatedImage: string | null
  isGenerating: boolean
  error: string | null
}

export function ResultSection({ generatedImage, isGenerating, error }: ResultSectionProps) {
  const downloadImage = () => {
    if (!generatedImage) return

    const link = document.createElement("a")
    link.href = generatedImage
    link.download = "preview-apartamento.png"
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
  }

  if (!generatedImage && !isGenerating && !error) {
    return null
  }

  return (
    <div className="mt-12">
      <Card className="overflow-hidden">
        <CardHeader className="bg-gray-50 border-b">
          <CardTitle className="flex items-center gap-2 text-xl">
            <Eye className="w-5 h-5 text-emerald-600" />
            Preview Gerado
          </CardTitle>
        </CardHeader>
        <CardContent className="p-6">
          {isGenerating && (
            <div className="flex flex-col items-center justify-center py-12 space-y-4">
              <div className="w-12 h-12 border-4 border-emerald-200 border-t-emerald-600 rounded-full animate-spin" />
              <div className="text-center">
                <p className="text-lg font-medium text-gray-900">Gerando seu preview do apartamento...</p>
                <p className="text-gray-600 mt-1">Isso pode levar alguns momentos</p>
              </div>
            </div>
          )}

          {error && (
            <div className="flex flex-col items-center justify-center py-12 space-y-4">
              <div className="w-12 h-12 bg-red-100 rounded-full flex items-center justify-center">
                <X className="w-6 h-6 text-red-600" />
              </div>
              <div className="text-center">
                <p className="text-lg font-medium text-red-900">Falha na Geração</p>
                <p className="text-red-600 mt-1">{error}</p>
              </div>
            </div>
          )}

          {generatedImage && !isGenerating && (
            <div className="space-y-6">
              <div className="relative rounded-lg overflow-hidden bg-gray-100">
                <Image
                  src={generatedImage || "/placeholder.svg"}
                  alt="Preview do apartamento gerado"
                  width={800}
                  height={600}
                  className="w-full h-auto object-contain"
                  priority
                />
              </div>

              <div className="flex justify-center gap-4">
                <Button onClick={downloadImage} variant="outline" className="flex items-center gap-2 bg-transparent">
                  <Download className="w-4 h-4" />
                  Baixar Preview
                </Button>
              </div>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  )
}
