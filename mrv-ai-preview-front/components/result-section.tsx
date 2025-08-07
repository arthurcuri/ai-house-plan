"use client"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Download, Eye, X, Sparkles, Clock } from "lucide-react"
import Image from "next/image"

interface ResultSectionProps {
  generatedImage: string | null
  generatedImages: any[]
  isGenerating: boolean
  isGeneratingImages: boolean
  error: string | null
  onGenerateImages?: () => void
  previewData?: any
}

export function ResultSection({ 
  generatedImage, 
  generatedImages, 
  isGenerating, 
  isGeneratingImages, 
  error, 
  onGenerateImages,
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

  if (!generatedImage && !generatedImages.length && !isGenerating && !isGeneratingImages && !error) {
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
                        <div>
                          <span className="font-medium">Cômodos encontrados:</span>
                          <p className="text-gray-600 mt-1">
                            {JSON.parse(previewData.interpretacao_llm)?.cômodos?.length || 'N/A'} cômodos detectados
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
                  
                  {onGenerateImages && !isGeneratingImages && (
                    <Button 
                      onClick={onGenerateImages}
                      className="flex items-center gap-2 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-700 hover:to-teal-700"
                    >
                      <Sparkles className="w-4 h-4" />
                      Gerar Imagens 3D HD
                    </Button>
                  )}
                </div>
              </div>
            )}
          </CardContent>
        </Card>
      )}

      {/* HD Images Generation Section */}
      {(isGeneratingImages || generatedImages.length > 0) && (
        <Card className="overflow-hidden">
          <CardHeader className="bg-gradient-to-r from-emerald-50 to-teal-50 border-b">
            <CardTitle className="flex items-center gap-2 text-xl">
              <Sparkles className="w-5 h-5 text-emerald-600" />
              Imagens 3D em Alta Definição
            </CardTitle>
          </CardHeader>
          <CardContent className="p-6">
            {isGeneratingImages && (
              <div className="flex flex-col items-center justify-center py-12 space-y-4">
                <div className="w-12 h-12 border-4 border-emerald-200 border-t-emerald-600 rounded-full animate-spin" />
                <div className="text-center">
                  <p className="text-lg font-medium text-gray-900">Gerando imagens 3D em alta qualidade...</p>
                  <p className="text-gray-600 mt-1">Este processo pode levar alguns minutos</p>
                  <div className="flex items-center gap-2 mt-2 text-sm text-gray-500">
                    <Clock className="w-4 h-4" />
                    Renderização fotorrealística com ray tracing
                  </div>
                </div>
              </div>
            )}

            {generatedImages.length > 0 && (
              <div className="space-y-6">
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                  {generatedImages.map((image, index) => (
                    <div key={index} className="space-y-3">
                      {image.erro ? (
                        <div className="bg-red-50 border border-red-200 rounded-lg p-4">
                          <p className="text-red-800 font-medium">{image.comodo}</p>
                          <p className="text-red-600 text-sm mt-1">{image.erro}</p>
                        </div>
                      ) : (
                        <>
                          <div className="relative rounded-lg overflow-hidden bg-gray-100 aspect-square">
                            {image.arquivo && (
                              <Image
                                src={`http://127.0.0.1:8000${image.url_relativa}`}
                                alt={`Cômodo: ${image.comodo}`}
                                fill
                                className="object-cover"
                                onError={(e) => {
                                  console.error('Erro ao carregar imagem:', e)
                                }}
                              />
                            )}
                          </div>
                          <div className="space-y-2">
                            <h4 className="font-semibold text-gray-900">{image.comodo}</h4>
                            <div className="flex flex-wrap gap-2 text-xs text-gray-600">
                              <span className="bg-gray-100 px-2 py-1 rounded">
                                {(image.tamanho_bytes / 1024).toFixed(0)}KB
                              </span>
                              {image.alta_qualidade && (
                                <span className="bg-emerald-100 text-emerald-700 px-2 py-1 rounded">
                                  HD
                                </span>
                              )}
                              {image.tempo_geracao && (
                                <span className="bg-blue-100 text-blue-700 px-2 py-1 rounded">
                                  {image.tempo_geracao.toFixed(1)}s
                                </span>
                              )}
                            </div>
                            {image.dimensoes && (
                              <p className="text-xs text-gray-500">
                                {image.dimensoes.largura}cm × {image.dimensoes.comprimento}cm
                              </p>
                            )}
                            <Button
                              size="sm"
                              variant="outline"
                              onClick={() => downloadGeneratedImage(
                                `http://127.0.0.1:8000${image.url_relativa}`,
                                `${image.comodo}.jpg`
                              )}
                              className="w-full"
                            >
                              <Download className="w-3 h-3 mr-1" />
                              Baixar
                            </Button>
                          </div>
                        </>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            )}
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
