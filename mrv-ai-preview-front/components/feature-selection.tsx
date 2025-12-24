"use client"

import { useRouter } from "next/navigation"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Building2, Palette, ArrowRight } from "lucide-react"

interface FeatureSelectionProps {
  onBack?: () => void
}

export function FeatureSelection({ onBack }: FeatureSelectionProps) {
  const router = useRouter()

  const handleSelectFeature = (feature: "arquiteto" | "preview") => {
    if (feature === "arquiteto") {
      router.push("/arquiteto")
    } else {
      router.push("/preview")
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-emerald-50 via-white to-orange-50">
      <div className="container mx-auto px-4 py-12">
        {onBack && (
          <Button
            variant="ghost"
            onClick={onBack}
            className="mb-8 text-gray-600 hover:text-emerald-600"
          >
            ← Voltar
          </Button>
        )}

        <div className="max-w-4xl mx-auto space-y-8">
          <div className="text-center space-y-4 mb-12">
            <h1 className="text-4xl lg:text-5xl font-bold text-gray-900">
              Escolha uma Funcionalidade
            </h1>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Selecione a ferramenta que deseja utilizar
            </p>
          </div>

          <div className="grid md:grid-cols-2 gap-6">
            {/* Área do Arquiteto */}
            <Card
              className="cursor-pointer hover:shadow-lg transition-all duration-300 border-2 hover:border-emerald-500 group"
              onClick={() => handleSelectFeature("arquiteto")}
            >
              <CardHeader className="pb-4">
                <div className="w-16 h-16 bg-gradient-to-br from-emerald-500 to-emerald-600 rounded-lg flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                  <Palette className="w-8 h-8 text-white" />
                </div>
                <CardTitle className="text-2xl text-gray-900">Área do Arquiteto</CardTitle>
                <CardDescription className="text-base mt-2">
                  Crie tipos pessoais de arquitetura a partir de suas fotos de projetos reais
                </CardDescription>
              </CardHeader>
              <CardContent>
                <ul className="space-y-2 text-sm text-gray-600 mb-6">
                  <li className="flex items-start gap-2">
                    <span className="text-emerald-600 mt-1">•</span>
                    <span>Envie fotos de seus projetos</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <span className="text-emerald-600 mt-1">•</span>
                    <span>IA analisa e cria prompts personalizados</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <span className="text-emerald-600 mt-1">•</span>
                    <span>Use seus tipos em todas as features</span>
                  </li>
                </ul>
                <Button
                  className="w-full bg-emerald-600 hover:bg-emerald-700 text-white group-hover:bg-emerald-700"
                  onClick={(e) => {
                    e.stopPropagation()
                    handleSelectFeature("arquiteto")
                  }}
                >
                  Acessar Área do Arquiteto
                  <ArrowRight className="w-4 h-4 ml-2" />
                </Button>
              </CardContent>
            </Card>

            {/* Preview da Planta */}
            <Card
              className="cursor-pointer hover:shadow-lg transition-all duration-300 border-2 hover:border-emerald-500 group"
              onClick={() => handleSelectFeature("preview")}
            >
              <CardHeader className="pb-4">
                <div className="w-16 h-16 bg-gradient-to-br from-orange-500 to-orange-600 rounded-lg flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                  <Building2 className="w-8 h-8 text-white" />
                </div>
                <CardTitle className="text-2xl text-gray-900">Preview da Planta</CardTitle>
                <CardDescription className="text-base mt-2">
                  Gere visualizações fotorrealistas a partir de sua planta baixa
                </CardDescription>
              </CardHeader>
              <CardContent>
                <ul className="space-y-2 text-sm text-gray-600 mb-6">
                  <li className="flex items-start gap-2">
                    <span className="text-orange-600 mt-1">•</span>
                    <span>Envie sua planta baixa</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <span className="text-orange-600 mt-1">•</span>
                    <span>Escolha o tipo de apartamento</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <span className="text-orange-600 mt-1">•</span>
                    <span>Receba imagens 3D fotorrealistas</span>
                  </li>
                </ul>
                <Button
                  className="w-full bg-orange-600 hover:bg-orange-700 text-white group-hover:bg-orange-700"
                  onClick={(e) => {
                    e.stopPropagation()
                    handleSelectFeature("preview")
                  }}
                >
                  Gerar Preview
                  <ArrowRight className="w-4 h-4 ml-2" />
                </Button>
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </div>
  )
}

