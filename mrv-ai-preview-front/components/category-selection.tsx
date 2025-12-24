"use client"
import { useState, useEffect } from "react"
import { Card, CardContent } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Crown, Leaf, Recycle, Home, Check, Palette } from "lucide-react"
import { images } from "@/lib/images"
import { TokenManager } from "@/lib/token-manager"

interface CategorySelectionProps {
  selectedCategory: string | null
  selectedPersonalType: number | null
  onCategorySelect: (category: string | null) => void
  onPersonalTypeSelect: (personalTypeId: number | null) => void
}

interface PersonalType {
  id: number
  nome: string
  status: string
  prompts_gerados: boolean
}

export function CategorySelection({ 
  selectedCategory, 
  selectedPersonalType,
  onCategorySelect, 
  onPersonalTypeSelect 
}: CategorySelectionProps) {
  const [personalTypes, setPersonalTypes] = useState<PersonalType[]>([])
  const [isLoadingTypes, setIsLoadingTypes] = useState(false)

  useEffect(() => {
    loadPersonalTypes()
  }, [])

  const loadPersonalTypes = async () => {
    setIsLoadingTypes(true)
    try {
      const token = TokenManager.getToken()
      if (!token) return

      const response = await fetch("/api/architect/types", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })

      if (response.ok) {
        const data = await response.json()
        // Filtrar apenas tipos concluídos e com prompts gerados
        const tiposDisponiveis = (data.tipos || []).filter(
          (t: PersonalType) => t.status === "concluido" && t.prompts_gerados
        )
        setPersonalTypes(tiposDisponiveis)
      }
    } catch (error) {
      console.error("Erro ao carregar tipos pessoais:", error)
    } finally {
      setIsLoadingTypes(false)
    }
  }

  const handleCategorySelect = (categoryId: string) => {
    onCategorySelect(categoryId)
    onPersonalTypeSelect(null) // Limpar seleção de tipo pessoal
  }

  const handlePersonalTypeSelect = (typeId: string) => {
    if (typeId === "none") {
      onPersonalTypeSelect(null)
    } else {
      onPersonalTypeSelect(parseInt(typeId))
      onCategorySelect(null) // Limpar seleção de categoria padrão
    }
  }

  const categories = [
    {
      id: "essential",
      name: "Essential",
      description: "Apartamentos confortáveis e funcionais com todas as comodidades básicas",
      icon: <Home className="w-8 h-8" />,
      color: "from-blue-500 to-blue-600",
      bgColor: "bg-blue-50",
      textColor: "text-blue-700",
      borderColor: "border-blue-200",
      features: ["Design moderno", "Acabamentos de qualidade", "Ótima localização"],
    },
    {
      id: "eco",
      name: "Eco",
      description: "Vida ambientalmente consciente com soluções de energia renovável",
      icon: <Recycle className="w-8 h-8" />,
      color: "from-emerald-500 to-emerald-600",
      bgColor: "bg-emerald-50",
      textColor: "text-emerald-700",
      borderColor: "border-emerald-200",
      features: ["Painéis solares", "Reciclagem de água", "Sistemas inteligentes"],
    },
    {
      id: "bio",
      name: "Bio",
      description: "Apartamentos ecológicos com materiais sustentáveis e áreas verdes",
      icon: <Leaf className="w-8 h-8" />,
      color: "from-green-500 to-green-600",
      bgColor: "bg-green-50",
      textColor: "text-green-700",
      borderColor: "border-green-200",
      features: ["Materiais sustentáveis", "Áreas verdes", "Eficiência energética"],
    },
    
    {
      id: "class",
      name: "Class",
      description: "Apartamentos premium com acabamentos de luxo e comodidades exclusivas",
      icon: <Crown className="w-8 h-8" />,
      color: "from-purple-500 to-purple-600",
      bgColor: "bg-purple-50",
      textColor: "text-purple-700",
      borderColor: "border-purple-200",
      features: ["Acabamentos premium", "Comodidades exclusivas", "Serviço de concierge"],
    }
  ]

  return (
    <div className="space-y-6">
      <div className="text-center">
        <h2 className="text-2xl font-bold text-gray-900 mb-2">Selecione a Categoria do Apartamento</h2>
        <p className="text-gray-600">Escolha o tipo de apartamento para gerar uma visualização mais precisa</p>
      </div>

      <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-4">
        {categories.map((category) => (
          <Card
            key={category.id}
            className={`cursor-pointer transition-all duration-300 hover:shadow-lg transform hover:-translate-y-1 ${
              selectedCategory === category.id
                ? `ring-2 ring-emerald-500 shadow-lg ${category.borderColor}`
                : "border-gray-200 hover:border-gray-300"
            }`}
            onClick={() => handleCategorySelect(category.id)}
          >
            <CardContent className="p-6 text-center space-y-4">
              {/* Selection Indicator */}
              {selectedCategory === category.id && (
                <div className="absolute top-3 right-3">
                  <div className="w-6 h-6 bg-emerald-500 rounded-full flex items-center justify-center">
                    <Check className="w-4 h-4 text-white" />
                  </div>
                </div>
              )}

              {/* Icon */}
              <div
                className={`w-16 h-16 mx-auto rounded-full bg-gradient-to-br ${category.color} flex items-center justify-center text-white`}
              >
                {category.icon}
              </div>

              {/* Title */}
              <div>
                <h3 className="text-xl font-bold text-gray-900 mb-2">{category.name}</h3>
                <p className="text-sm text-gray-600 leading-relaxed">{category.description}</p>
              </div>

              {/* Features */}
              <div className="space-y-2">
                {category.features.map((feature, index) => (
                  <Badge
                    key={index}
                    variant="secondary"
                    className={`${category.bgColor} ${category.textColor} border-0 text-xs`}
                  >
                    {feature}
                  </Badge>
                ))}
              </div>

              {/* Selection State */}
              <div className="pt-2">
                {selectedCategory === category.id ? (
                  <div className="text-emerald-600 font-medium text-sm">✓ Selecionado</div>
                ) : (
                  <div className="text-gray-400 text-sm">Clique para selecionar</div>
                )}
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Seção de Tipo Pessoal */}
      <div className="space-y-4 pt-6 border-t border-gray-200">
        <div className="text-center">
          <h3 className="text-lg font-semibold text-gray-900 mb-2 flex items-center justify-center gap-2">
            <Palette className="w-5 h-5 text-emerald-600" />
            Ou escolha um tipo pessoal
          </h3>
          <p className="text-sm text-gray-600 mb-4">
            Use um estilo arquitetônico personalizado criado na Área do Arquiteto
          </p>
        </div>

        <div className="max-w-md mx-auto">
          <Select
            value={selectedPersonalType?.toString() || "none"}
            onValueChange={handlePersonalTypeSelect}
            disabled={isLoadingTypes}
          >
            <SelectTrigger className="w-full">
              <SelectValue placeholder="Selecione um tipo pessoal" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="none">Nenhum (usar categoria padrão)</SelectItem>
              {personalTypes.length === 0 && !isLoadingTypes && (
                <SelectItem value="empty" disabled>
                  Nenhum tipo pessoal disponível
                </SelectItem>
              )}
              {isLoadingTypes && (
                <SelectItem value="loading" disabled>
                  Carregando tipos...
                </SelectItem>
              )}
              {personalTypes.map((type) => (
                <SelectItem key={type.id} value={type.id.toString()}>
                  {type.nome}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>
      </div>

      {/* Indicadores de Seleção */}
      {(selectedCategory || selectedPersonalType) && (
        <div className="text-center">
          <div className="inline-flex items-center gap-2 bg-emerald-100 text-emerald-800 px-4 py-2 rounded-full text-sm font-medium">
            <Check className="w-4 h-4" />
            {selectedCategory
              ? `Categoria ${categories.find((c) => c.id === selectedCategory)?.name} selecionada`
              : selectedPersonalType
              ? `Tipo pessoal "${personalTypes.find((t) => t.id === selectedPersonalType)?.nome}" selecionado`
              : ""}
          </div>
        </div>
      )}
    </div>
  )
}
