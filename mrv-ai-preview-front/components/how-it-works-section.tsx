import { Card, CardContent } from "@/components/ui/card"
import { Upload, Cpu, ImageIcon } from "lucide-react"

export function HowItWorksSection() {
  const steps = [
    {
      step: "01",
      icon: <Upload className="w-8 h-8 text-white" />,
      title: "Upload Your Floor Plan",
      description:
        "Simply drag and drop your apartment floor plan or select it from your device. We support all common image and PDF formats.",
    },
    {
      step: "02",
      icon: <Cpu className="w-8 h-8 text-white" />,
      title: "AI Analyzes Structure",
      description:
        "Our advanced AI algorithms analyze the architectural layout, room dimensions, and spatial relationships in your floor plan.",
    },
    {
      step: "03",
      icon: <ImageIcon className="w-8 h-8 text-white" />,
      title: "Receive Realistic Preview",
      description:
        "Get a stunning, photorealistic 3D-style visualization of your apartment in seconds, ready to download and share.",
    },
  ]

  return (
    <section id="how-it-works" className="py-20 bg-gray-50">
      <div className="container mx-auto px-4">
        <div className="text-center mb-16">
          <h2 className="text-3xl lg:text-4xl font-bold text-gray-900 mb-6">How It Works</h2>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Transform your floor plans into realistic previews in just three simple steps
          </p>
        </div>

        <div className="grid lg:grid-cols-3 gap-8">
          {steps.map((step, index) => (
            <div key={index} className="relative">
              <Card className="border-0 shadow-lg hover:shadow-xl transition-shadow duration-300 h-full">
                <CardContent className="p-8 text-center">
                  <div className="flex justify-center mb-6">
                    <div className="w-16 h-16 bg-emerald-600 rounded-full flex items-center justify-center">
                      {step.icon}
                    </div>
                  </div>
                  <div className="text-emerald-600 font-bold text-lg mb-2">{step.step}</div>
                  <h3 className="text-xl font-semibold text-gray-900 mb-4">{step.title}</h3>
                  <p className="text-gray-600 leading-relaxed">{step.description}</p>
                </CardContent>
              </Card>

              {/* Arrow for desktop */}
              {index < steps.length - 1 && (
                <div className="hidden lg:block absolute top-1/2 -right-4 transform -translate-y-1/2 z-10">
                  <div className="w-8 h-8 bg-emerald-200 rounded-full flex items-center justify-center">
                    <div className="w-4 h-4 border-r-2 border-b-2 border-emerald-600 transform rotate-[-45deg]" />
                  </div>
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
