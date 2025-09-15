"use client"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Download, Eye, X, ImageIcon } from "lucide-react"
import Image from "next/image"

interface ResultSectionProps {
  generatedImage: string | null
  generatedImages: any[]
  isGenerating: boolean
  error: string | null
  previewData?: any
}

export function ResultSection({ 
  generatedImage, 
  generatedImages,
  isGenerating, 
  error, 
  previewData 
}: ResultSectionProps) {
  const downloadImage = () => {
    if (!generatedImage) return

    const link = document.createElement("a")
    link.href = generatedImage
    link.download = "preview-apartamento.png"
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
  }

  const downloadGeneratedImage = (imageUrl: string, filename: string) => {
    const link = document.createElement("a")
    link.href = imageUrl
    link.download = filename
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
  }

  // Função auxiliar para extrair JSON válido de resposta que pode conter markdown
  function parseInterpretation(interpretationText: string) {
    try {
      // Se já é um objeto, retorna direto
      if (typeof interpretationText === 'object') {
        return interpretationText
      }
      
      // Tentar parse direto primeiro
      return JSON.parse(interpretationText)
    } catch {
      try {
        // Extrair JSON de dentro de markdown code blocks
        const jsonMatch = interpretationText.match(/```json\s*([\s\S]*?)\s*```/)
        if (jsonMatch) {
          return JSON.parse(jsonMatch[1])
        }
        
        // Tentar encontrar JSON sem code blocks
        const jsonStart = interpretationText.indexOf('{')
        const jsonEnd = interpretationText.lastIndexOf('}')
        
        if (jsonStart !== -1 && jsonEnd !== -1 && jsonEnd > jsonStart) {
          const jsonStr = interpretationText.substring(jsonStart, jsonEnd + 1)
          return JSON.parse(jsonStr)
        }
        
        return null
      } catch {
        return null
      }
    }
  }

  if (!generatedImage && !generatedImages.length && !isGenerating && !error) {
    return null
  }

  return (
    <div className="mt-12 space-y-6">
      {/* Preview Section */}
      {(generatedImage || isGenerating) && (
        <Card className="overflow-hidden">
          <CardHeader className="bg-gray-50 border-b">
            <CardTitle className="flex items-center gap-2 text-xl">
              <Eye className="w-5 h-5 text-emerald-600" />
              Preview da Planta
            </CardTitle>
          </CardHeader>
          <CardContent className="p-6">
            {isGenerating && (
              <div className="flex flex-col items-center justify-center py-12 space-y-4">
                <div className="w-12 h-12 border-4 border-emerald-200 border-t-emerald-600 rounded-full animate-spin" />
                <div className="text-center">
                  <p className="text-lg font-medium text-gray-900">Analisando sua planta...</p>
                  <p className="text-gray-600 mt-1">Extraindo informações dos cômodos</p>
                </div>
              </div>
            )}

            {generatedImage && !isGenerating && (
              <div className="space-y-6">
                <div className="relative rounded-lg overflow-hidden bg-gray-100">
                  <Image
                    src={generatedImage || "/placeholder.svg"}
                    alt="Preview da planta analisada"
                    width={800}
                    height={600}
                    className="w-full h-auto object-contain"
                    priority
                  />
                </div>

                {previewData && (
                  <div className="bg-gray-50 rounded-lg p-4">
                    <h3 className="font-semibold text-gray-900 mb-2">Informações Detectadas:</h3>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                      {previewData.interpretacao_llm && (
                        <div className="border rounded-lg p-4 bg-gray-50">
                          <span className="font-medium">Cômodos encontrados:</span>
                          <p className="text-gray-600 mt-1">
                            {(() => {
                              const parsed = parseInterpretation(previewData.interpretacao_llm)
                              return parsed?.cômodos?.length || parsed?.comodos?.length || 'N/A'
                            })()} cômodos detectados
                          </p>
                        </div>
                      )}
                      <div>
                        <span className="font-medium">Texto extraído (OCR):</span>
                        <p className="text-gray-600 mt-1">
                          {previewData.textos_extraidos?.slice(0, 3).join(', ') || 'Nenhum texto detectado'}
                        </p>
                      </div>
                    </div>
                  </div>
                )}

                <div className="flex justify-center gap-4">
                  <Button onClick={downloadImage} variant="outline" className="flex items-center gap-2">
                    <Download className="w-4 h-4" />
                    Baixar Preview
                  </Button>
                </div>
              </div>
            )}
          </CardContent>
        </Card>
      )}

      {/* Generated Images Catalog */}
      {generatedImages.length > 0 && (
        <Card className="overflow-hidden">
          <CardHeader className="bg-gradient-to-r from-emerald-50 to-teal-50 border-b">
            <CardTitle className="flex items-center gap-2 text-xl">
              <ImageIcon className="w-5 h-5 text-emerald-600" />
              Álbum de Ambientes Gerados
              <span className="text-sm font-normal text-gray-600">
                ({generatedImages.length} {generatedImages.length === 1 ? 'ambiente' : 'ambientes'})
              </span>
            </CardTitle>
            <p className="text-sm text-gray-500 mt-1">
              Imagens geradas em alta qualidade para cada cômodo identificado na planta
            </p>
          </CardHeader>
          <CardContent className="p-6">
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {generatedImages.map((image, index) => (
                <div key={index} className="space-y-3">
                  <div className="relative rounded-lg overflow-hidden bg-gray-100 aspect-square group">
                    <Image
                      src={image.url}
                      alt={image.name || `Ambiente ${index + 1}`}
                      fill
                      className="object-cover transition-transform group-hover:scale-105"
                      onError={(e) => {
                        console.error('Erro ao carregar imagem:', e)
                        console.error('URL da imagem:', image.url)
                      }}
                    />
                    <div className="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-20 transition-opacity" />
                    {image.fileSize && (
                      <div className="absolute top-2 right-2 bg-black bg-opacity-70 text-white text-xs px-2 py-1 rounded">
                        {(image.fileSize / 1024).toFixed(0)}KB
                      </div>
                    )}
                  </div>
                  <div className="space-y-2">
                    <h4 className="font-semibold text-gray-900">
                      {image.name || image.room || `Ambiente ${index + 1}`}
                    </h4>
                    {image.location && (
                      <p className="text-sm text-gray-600">
                        <span className="font-medium">Localização:</span> {image.location}
                      </p>
                    )}
                    <div className="flex flex-wrap gap-2 text-xs">
                      <span className="bg-emerald-100 text-emerald-700 px-2 py-1 rounded-full">
                        {image.category}
                      </span>
                      {image.room && (
                        <span className="bg-blue-100 text-blue-700 px-2 py-1 rounded-full">
                          {image.room}
                        </span>
                      )}
                      <span className="bg-gray-100 text-gray-700 px-2 py-1 rounded-full">
                        3D HD
                      </span>
                    </div>
                    {image.notes && (
                      <p className="text-xs text-gray-500 line-clamp-2" title={image.notes}>
                        {image.notes}
                      </p>
                    )}
                    <Button
                      size="sm"
                      variant="outline"
                      onClick={() => downloadGeneratedImage(
                        image.url,
                        `${image.name || image.room || `ambiente_${index + 1}`}.png`
                      )}
                      className="w-full"
                    >
                      <Download className="w-3 h-3 mr-1" />
                      Baixar Imagem HD
                    </Button>
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      )}

      {/* Error Section */}
      {error && (
        <Card className="overflow-hidden">
          <CardContent className="p-6">
            <div className="flex flex-col items-center justify-center py-12 space-y-4">
              <div className="w-12 h-12 bg-red-100 rounded-full flex items-center justify-center">
                <X className="w-6 h-6 text-red-600" />
              </div>
              <div className="text-center">
                <p className="text-lg font-medium text-red-900">Erro na Geração</p>
                <p className="text-red-600 mt-1">{error}</p>
              </div>
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  )
}
