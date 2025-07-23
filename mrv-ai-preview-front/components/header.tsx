"use client"

import { useState } from "react"
import { Building2, Menu, X } from "lucide-react"
import { Button } from "@/components/ui/button"

export function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)

  const scrollToSection = (sectionId: string) => {
    const element = document.getElementById(sectionId)
    if (element) {
      element.scrollIntoView({ behavior: "smooth" })
    }
    setIsMenuOpen(false)
  }

  return (
    <header className="bg-white border-b border-gray-100 shadow-sm sticky top-0 z-50">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <div className="flex items-center gap-3">
            <div className="flex items-center gap-2">
              <div className="w-8 h-8 bg-gradient-to-br from-emerald-500 to-emerald-600 rounded-lg flex items-center justify-center">
                <Building2 className="w-5 h-5 text-white" />
              </div>
              <div className="w-8 h-8 bg-gradient-to-br from-orange-500 to-orange-600 rounded-lg flex items-center justify-center transform rotate-45">
                <div className="w-3 h-3 bg-white rounded-sm transform -rotate-45" />
              </div>
            </div>
            <span className="text-xl font-bold text-gray-900">MRV AI Preview</span>
          </div>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex items-center gap-8">
            <button
              onClick={() => scrollToSection("about")}
              className="text-gray-600 hover:text-emerald-600 transition-colors"
            >
              About
            </button>
            <button
              onClick={() => scrollToSection("how-it-works")}
              className="text-gray-600 hover:text-emerald-600 transition-colors"
            >
              How It Works
            </button>
            <button
              onClick={() => scrollToSection("showcase")}
              className="text-gray-600 hover:text-emerald-600 transition-colors"
            >
              Examples
            </button>
            <button
              onClick={() => scrollToSection("faq")}
              className="text-gray-600 hover:text-emerald-600 transition-colors"
            >
              FAQ
            </button>
            <Button onClick={() => scrollToSection("hero")} className="bg-emerald-600 hover:bg-emerald-700 text-white">
              Try Now
            </Button>
          </nav>

          {/* Mobile Menu Button */}
          <button
            onClick={() => setIsMenuOpen(!isMenuOpen)}
            className="md:hidden p-2 text-gray-600 hover:text-emerald-600"
          >
            {isMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
          </button>
        </div>

        {/* Mobile Navigation */}
        {isMenuOpen && (
          <div className="md:hidden py-4 border-t border-gray-100">
            <nav className="flex flex-col gap-4">
              <button
                onClick={() => scrollToSection("about")}
                className="text-left text-gray-600 hover:text-emerald-600 transition-colors"
              >
                About
              </button>
              <button
                onClick={() => scrollToSection("how-it-works")}
                className="text-left text-gray-600 hover:text-emerald-600 transition-colors"
              >
                How It Works
              </button>
              <button
                onClick={() => scrollToSection("showcase")}
                className="text-left text-gray-600 hover:text-emerald-600 transition-colors"
              >
                Examples
              </button>
              <button
                onClick={() => scrollToSection("faq")}
                className="text-left text-gray-600 hover:text-emerald-600 transition-colors"
              >
                FAQ
              </button>
              <Button
                onClick={() => scrollToSection("hero")}
                className="bg-emerald-600 hover:bg-emerald-700 text-white w-full mt-2"
              >
                Try Now
              </Button>
            </nav>
          </div>
        )}
      </div>
    </header>
  )
}
