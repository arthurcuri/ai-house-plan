"use client"

import { useState } from "react"
import { Card, CardContent } from "@/components/ui/card"
import { ChevronDown, ChevronUp } from "lucide-react"

export function FAQSection() {
  const [openFAQ, setOpenFAQ] = useState<number | null>(0)

  const faqs = [
    {
      question: "Quais formatos de arquivo são suportados para plantas baixas?",
      answer:
        "O MRV AI Preview suporta todos os formatos de imagem comuns incluindo PNG, JPG, JPEG e arquivos PDF. Recomendamos imagens de alta resolução para melhores resultados.",
    },
    {
      question: "Quanto tempo leva para gerar um preview?",
      answer:
        "Nossa IA normalmente gera previews realistas de apartamentos em menos de 30 segundos. O tempo de processamento pode variar ligeiramente dependendo da complexidade da sua planta baixa.",
    },
    {
      question: "Quão precisos são os previews gerados por IA?",
      answer:
        "Nossa IA cria visualizações altamente realistas baseadas em melhores práticas arquitetônicas e padrões de design. Embora os previews sejam fotorrealistas, eles representam uma possível interpretação da sua planta baixa.",
    },
    {
      question: "Posso personalizar o preview gerado?",
      answer:
        "Atualmente, nossa IA gera previews automaticamente baseados na estrutura da planta baixa. Estamos trabalhando em adicionar opções de personalização para estilos de móveis, esquemas de cores e acabamentos em futuras atualizações.",
    },
  ]

  const toggleFAQ = (index: number) => {
    setOpenFAQ(openFAQ === index ? null : index)
  }

  return (
    <section id="faq" className="py-20 bg-gray-50">
      <div className="container mx-auto px-4">
        <div className="text-center mb-16">
          <h2 className="text-3xl lg:text-4xl font-bold text-gray-900 mb-6">Perguntas Frequentes</h2>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Obtenha respostas para perguntas comuns sobre o MRV AI Preview
          </p>
        </div>

        <div className="max-w-3xl mx-auto space-y-4">
          {faqs.map((faq, index) => (
            <Card key={index} className="border-0 shadow-lg">
              <CardContent className="p-0">
                <button
                  onClick={() => toggleFAQ(index)}
                  className="w-full p-6 text-left flex items-center justify-between hover:bg-gray-50 transition-colors"
                >
                  <h3 className="text-lg font-semibold text-gray-900 pr-4">{faq.question}</h3>
                  {openFAQ === index ? (
                    <ChevronUp className="w-5 h-5 text-emerald-600 flex-shrink-0" />
                  ) : (
                    <ChevronDown className="w-5 h-5 text-gray-400 flex-shrink-0" />
                  )}
                </button>
                {openFAQ === index && (
                  <div className="px-6 pb-6">
                    <p className="text-gray-600 leading-relaxed">{faq.answer}</p>
                  </div>
                )}
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  )
}
