"use client"

import { useState } from "react"
import { Card, CardContent } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { ChevronLeft, ChevronRight } from "lucide-react"
import Image from "next/image"

export function PreviewShowcase() {
  const [currentSlide, setCurrentSlide] = useState(0)

  const showcaseItems = [
    {
      before: "/placeholder.svg?height=300&width=400&text=Planta+Baixa+1",
      after: "/placeholder.svg?height=300&width=400&text=Apartamento+3D+1",
      title: "Apartamento Studio Moderno",
      description: "Convertido de uma planta baixa simples para uma visualização 3D impressionante",
    },
    {
      before: "/placeholder.svg?height=300&width=400&text=Planta+Baixa+2",
      after: "/placeholder.svg?height=300&width=400&text=Apartamento+3D+2",
      title: "Layout de Dois Quartos",
      description: "Completo com disposição de móveis e iluminação realista",
    },
    {
      before: "/placeholder.svg?height=300&width=400&text=Planta+Baixa+3",
      after: "/placeholder.svg?height=300&width=400&text=Apartamento+3D+3",
      title: "Cobertura de Luxo",
      description: "Visualização de acabamentos premium e materiais de alta qualidade",
    },
  ]

  const nextSlide = () => {
    setCurrentSlide((prev) => (prev + 1) % showcaseItems.length)
  }

  const prevSlide = () => {
    setCurrentSlide((prev) => (prev - 1 + showcaseItems.length) % showcaseItems.length)
  }

  return (
    <section id="showcase" className="py-20 bg-white">
      <div className="container mx-auto px-4">
        <div className="text-center mb-16">
          <h2 className="text-3xl lg:text-4xl font-bold text-gray-900 mb-6">Veja a Mágica em Ação</h2>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Descubra como nossa IA transforma plantas baixas simples em previews fotorrealistas impressionantes de
            apartamentos
          </p>
        </div>

        <div className="max-w-6xl mx-auto">
          <Card className="border-0 shadow-2xl overflow-hidden">
            <CardContent className="p-0">
              <div className="grid lg:grid-cols-2">
                {/* Before */}
                <div className="p-8 bg-gray-50">
                  <h3 className="text-xl font-semibold text-gray-900 mb-4">Antes: Planta Baixa</h3>
                  <div className="relative rounded-lg overflow-hidden bg-white shadow-lg">
                    <Image
                      src={showcaseItems[currentSlide].before || "/placeholder.svg"}
                      alt="Planta baixa original"
                      width={400}
                      height={300}
                      className="w-full h-64 object-cover"
                    />
                  </div>
                </div>

                {/* After */}
                <div className="p-8 bg-emerald-50">
                  <h3 className="text-xl font-semibold text-gray-900 mb-4">Depois: Preview IA</h3>
                  <div className="relative rounded-lg overflow-hidden bg-white shadow-lg">
                    <Image
                      src={showcaseItems[currentSlide].after || "/placeholder.svg"}
                      alt="Preview gerado por IA"
                      width={400}
                      height={300}
                      className="w-full h-64 object-cover"
                    />
                  </div>
                </div>
              </div>

              {/* Content */}
              <div className="p-8 text-center border-t border-gray-200">
                <h4 className="text-2xl font-semibold text-gray-900 mb-2">{showcaseItems[currentSlide].title}</h4>
                <p className="text-gray-600 mb-6">{showcaseItems[currentSlide].description}</p>

                {/* Navigation */}
                <div className="flex items-center justify-center gap-4">
                  <Button
                    variant="outline"
                    size="sm"
                    onClick={prevSlide}
                    className="border-emerald-200 text-emerald-700 hover:bg-emerald-50 bg-transparent"
                  >
                    <ChevronLeft className="w-4 h-4" />
                  </Button>

                  <div className="flex gap-2">
                    {showcaseItems.map((_, index) => (
                      <button
                        key={index}
                        onClick={() => setCurrentSlide(index)}
                        className={`w-3 h-3 rounded-full transition-colors ${
                          index === currentSlide ? "bg-emerald-600" : "bg-gray-300"
                        }`}
                      />
                    ))}
                  </div>

                  <Button
                    variant="outline"
                    size="sm"
                    onClick={nextSlide}
                    className="border-emerald-200 text-emerald-700 hover:bg-emerald-50 bg-transparent"
                  >
                    <ChevronRight className="w-4 h-4" />
                  </Button>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </section>
  )
}
