"use client"

import { Button } from "@/components/ui/button"
import { ArrowRight, Sparkles } from "lucide-react"
import { useAuth } from "@/hooks/use-auth"
import Image from "next/image"

interface HeroSectionProps {
  onTryNow: () => void
}

export function HeroSection({ onTryNow }: HeroSectionProps) {
  const { isAuthenticated } = useAuth()

  const scrollToLearnMore = () => {
    const element = document.getElementById("how-it-works")
    if (element) {
      element.scrollIntoView({ behavior: "smooth" })
    }
  }

  return (
    <section id="hero" className="relative bg-gradient-to-br from-emerald-50 via-white to-orange-50 py-20 lg:py-32">
      <div className="container mx-auto px-4">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* Left Column - Content */}
          <div className="space-y-8">
            <div className="space-y-4">
              <div className="inline-flex items-center gap-2 bg-emerald-100 text-emerald-800 px-4 py-2 rounded-full text-sm font-medium">
                <Sparkles className="w-4 h-4" />
                Powered by AI Technology
              </div>
              <h1 className="text-4xl lg:text-6xl font-bold text-gray-900 leading-tight">
                Transform Floor Plans into <span className="text-emerald-600">Realistic Previews</span> with AI
              </h1>
              <p className="text-xl text-gray-600 leading-relaxed max-w-lg">
                Experience your future apartment before it's built with MRV AI Preview. Get photorealistic
                visualizations in seconds.
              </p>
            </div>

            <div className="flex flex-col sm:flex-row gap-4">
              <Button
                onClick={onTryNow}
                size="lg"
                className="bg-emerald-600 hover:bg-emerald-700 text-white px-8 py-4 text-lg font-semibold"
              >
                {isAuthenticated ? "Open App" : "Try Now"}
                <ArrowRight className="w-5 h-5 ml-2" />
              </Button>
              <Button
                variant="outline"
                size="lg"
                onClick={scrollToLearnMore}
                className="border-emerald-200 text-emerald-700 hover:bg-emerald-50 px-8 py-4 text-lg bg-transparent"
              >
                Learn More
              </Button>
            </div>

            {/* Stats */}
            <div className="flex flex-wrap gap-8 pt-8 border-t border-gray-200">
              <div>
                <div className="text-2xl font-bold text-gray-900">10,000+</div>
                <div className="text-gray-600">Floor Plans Processed</div>
              </div>
              <div>
                <div className="text-2xl font-bold text-gray-900">&lt; 30s</div>
                <div className="text-gray-600">Average Generation Time</div>
              </div>
              <div>
                <div className="text-2xl font-bold text-gray-900">95%</div>
                <div className="text-gray-600">Customer Satisfaction</div>
              </div>
            </div>
          </div>

          {/* Right Column - Hero Image */}
          <div className="relative">
            <div className="relative rounded-2xl overflow-hidden shadow-2xl bg-white p-4">
              <Image
                src="/placeholder.svg?height=600&width=800&text=Modern+Apartment+Visualization"
                alt="AI-generated apartment preview"
                width={800}
                height={600}
                className="w-full h-auto rounded-lg"
                priority
              />
              <div className="absolute top-8 right-8 bg-white/90 backdrop-blur-sm rounded-lg px-3 py-2 shadow-lg">
                <div className="flex items-center gap-2">
                  <div className="w-2 h-2 bg-emerald-500 rounded-full animate-pulse" />
                  <span className="text-sm font-medium text-gray-700">AI Processing</span>
                </div>
              </div>
            </div>

            {/* Floating Elements */}
            <div className="absolute -top-4 -left-4 w-20 h-20 bg-orange-200 rounded-full opacity-60 animate-pulse" />
            <div className="absolute -bottom-6 -right-6 w-32 h-32 bg-emerald-200 rounded-full opacity-40 animate-pulse delay-1000" />
          </div>
        </div>
      </div>
    </section>
  )
}
