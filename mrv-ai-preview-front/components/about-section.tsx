import { Card, CardContent } from "@/components/ui/card"
import { Zap, Eye, Brain, Clock } from "lucide-react"

export function AboutSection() {
  const benefits = [
    {
      icon: <Zap className="w-8 h-8 text-emerald-600" />,
      title: "Upload de Qualquer Planta",
      description: "Suporte para todos os formatos comuns incluindo PNG, JPG e arquivos PDF",
    },
    {
      icon: <Eye className="w-8 h-8 text-emerald-600" />,
      title: "Visualização Fotorrealista",
      description: "Obtenha previews 3D impressionantes e realistas que parecem renders profissionais",
    },
    {
      icon: <Brain className="w-8 h-8 text-emerald-600" />,
      title: "Inteligência Artificial Avançada",
      description: "Algoritmos de machine learning avançados entendem layouts arquitetônicos e relações espaciais",
    },
    {
      icon: <Clock className="w-8 h-8 text-emerald-600" />,
      title: "Resultados Instantâneos",
      description: "Gere visualizações de qualidade profissional em segundos, não horas ou dias",
    },
  ]

  return (
    <section id="about" className="py-20 bg-white">
      <div className="container mx-auto px-4">
        <div className="text-center mb-16">
          <h2 className="text-3xl lg:text-4xl font-bold text-gray-900 mb-6">O que é o House AI Preview?</h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto leading-relaxed">
            O House AI Preview é uma ferramenta revolucionária que transforma plantas baixas simples em visualizações
            fotorrealistas impressionantes de apartamentos. Usando inteligência artificial de ponta, ajudamos você a ver
            exatamente como sua futura casa ficará antes mesmo da construção começar.
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          {benefits.map((benefit, index) => (
            <Card key={index} className="border-0 shadow-lg hover:shadow-xl transition-shadow duration-300">
              <CardContent className="p-8 text-center">
                <div className="flex justify-center mb-4">
                  <div className="w-16 h-16 bg-emerald-100 rounded-full flex items-center justify-center">
                    {benefit.icon}
                  </div>
                </div>
                <h3 className="text-xl font-semibold text-gray-900 mb-3">{benefit.title}</h3>
                <p className="text-gray-600 leading-relaxed">{benefit.description}</p>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  )
}
