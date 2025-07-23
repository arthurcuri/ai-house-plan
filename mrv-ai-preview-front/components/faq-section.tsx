"use client"

import { useState } from "react"
import { Card, CardContent } from "@/components/ui/card"
import { ChevronDown, ChevronUp } from "lucide-react"

export function FAQSection() {
  const [openFAQ, setOpenFAQ] = useState<number | null>(0)

  const faqs = [
    {
      question: "What file formats are supported for floor plans?",
      answer:
        "MRV AI Preview supports all common image formats including PNG, JPG, JPEG, and PDF files. We recommend high-resolution images for the best results.",
    },
    {
      question: "How long does it take to generate a preview?",
      answer:
        "Our AI typically generates realistic apartment previews in under 30 seconds. Processing time may vary slightly depending on the complexity of your floor plan.",
    },
    {
      question: "How accurate are the AI-generated previews?",
      answer:
        "Our AI creates highly realistic visualizations based on architectural best practices and design standards. While the previews are photorealistic, they represent one possible interpretation of your floor plan.",
    },
    {
      question: "Can I customize the generated preview?",
      answer:
        "Currently, our AI generates previews automatically based on the floor plan structure. We're working on adding customization options for furniture styles, color schemes, and finishes in future updates.",
    },
  ]

  const toggleFAQ = (index: number) => {
    setOpenFAQ(openFAQ === index ? null : index)
  }

  return (
    <section id="faq" className="py-20 bg-gray-50">
      <div className="container mx-auto px-4">
        <div className="text-center mb-16">
          <h2 className="text-3xl lg:text-4xl font-bold text-gray-900 mb-6">Frequently Asked Questions</h2>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Get answers to common questions about MRV AI Preview
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
