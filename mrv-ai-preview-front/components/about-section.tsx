import { Card, CardContent } from "@/components/ui/card"
import { Zap, Eye, Brain, Clock } from "lucide-react"

export function AboutSection() {
  const benefits = [
    {
      icon: <Zap className="w-8 h-8 text-emerald-600" />,
      title: "Upload Any Floor Plan",
      description: "Support for all common formats including PNG, JPG, and PDF files",
    },
    {
      icon: <Eye className="w-8 h-8 text-emerald-600" />,
      title: "Photorealistic Visualization",
      description: "Get stunning, realistic 3D-style apartment previews that look like professional renders",
    },
    {
      icon: <Brain className="w-8 h-8 text-emerald-600" />,
      title: "AI-Powered Intelligence",
      description: "Advanced machine learning algorithms understand architectural layouts and spatial relationships",
    },
    {
      icon: <Clock className="w-8 h-8 text-emerald-600" />,
      title: "Instant Results",
      description: "Generate professional-quality visualizations in seconds, not hours or days",
    },
  ]

  return (
    <section id="about" className="py-20 bg-white">
      <div className="container mx-auto px-4">
        <div className="text-center mb-16">
          <h2 className="text-3xl lg:text-4xl font-bold text-gray-900 mb-6">What is MRV AI Preview?</h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto leading-relaxed">
            MRV AI Preview is a revolutionary tool that transforms simple floor plans into stunning, photorealistic
            apartment visualizations. Using cutting-edge artificial intelligence, we help you see exactly how your
            future home will look before construction even begins.
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
