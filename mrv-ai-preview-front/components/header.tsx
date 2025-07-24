"use client"

import { useState } from "react"
import { Building2, Menu, X, User, LogOut, Settings } from "lucide-react"
import { Button } from "@/components/ui/button"
import { useAuth } from "@/hooks/use-auth"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import Link from "next/link"

interface HeaderProps {
  onTryNow?: () => void
}

export function Header({ onTryNow }: HeaderProps) {
  const [isMenuOpen, setIsMenuOpen] = useState(false)
  const { user, isAuthenticated, logout } = useAuth()

  const scrollToSection = (sectionId: string) => {
    const element = document.getElementById(sectionId)
    if (element) {
      element.scrollIntoView({ behavior: "smooth" })
    }
    setIsMenuOpen(false)
  }

  const handleLogout = () => {
    logout()
    setIsMenuOpen(false)
  }

  const getUserInitials = (name: string) => {
    return name
      .split(" ")
      .map((n) => n[0])
      .join("")
      .toUpperCase()
      .slice(0, 2)
  }

  return (
    <header className="bg-white border-b border-gray-100 shadow-sm sticky top-0 z-50">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link href="/" className="flex items-center gap-3">
            <div className="flex items-center gap-2">
              <div className="w-8 h-8 bg-gradient-to-br from-emerald-500 to-emerald-600 rounded-lg flex items-center justify-center">
                <Building2 className="w-5 h-5 text-white" />
              </div>
              <div className="w-8 h-8 bg-gradient-to-br from-orange-500 to-orange-600 rounded-lg flex items-center justify-center transform rotate-45">
                <div className="w-3 h-3 bg-white rounded-sm transform -rotate-45" />
              </div>
            </div>
            <span className="text-xl font-bold text-gray-900">MRV AI Preview</span>
          </Link>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex items-center gap-8">
            <button
              onClick={() => scrollToSection("about")}
              className="text-gray-600 hover:text-emerald-600 transition-colors"
            >
              Sobre
            </button>
            <button
              onClick={() => scrollToSection("how-it-works")}
              className="text-gray-600 hover:text-emerald-600 transition-colors"
            >
              Como Funciona
            </button>
            <button
              onClick={() => scrollToSection("showcase")}
              className="text-gray-600 hover:text-emerald-600 transition-colors"
            >
              Exemplos
            </button>
            <button
              onClick={() => scrollToSection("faq")}
              className="text-gray-600 hover:text-emerald-600 transition-colors"
            >
              FAQ
            </button>

            {/* Authentication Section */}
            {isAuthenticated ? (
              <DropdownMenu>
                <DropdownMenuTrigger asChild>
                  <Button variant="ghost" className="relative h-10 w-10 rounded-full">
                    <Avatar className="h-10 w-10">
                      <AvatarImage src={user?.avatar || "/placeholder.svg"} alt={user?.name} />
                      <AvatarFallback className="bg-emerald-100 text-emerald-700">
                        {user?.name ? getUserInitials(user.name) : "U"}
                      </AvatarFallback>
                    </Avatar>
                  </Button>
                </DropdownMenuTrigger>
                <DropdownMenuContent className="w-56" align="end" forceMount>
                  <div className="flex flex-col space-y-1 p-2">
                    <p className="text-sm font-medium leading-none">{user?.name}</p>
                    <p className="text-xs leading-none text-muted-foreground">{user?.email}</p>
                  </div>
                  <DropdownMenuSeparator />
                  <DropdownMenuItem onClick={onTryNow} className="cursor-pointer">
                    <User className="mr-2 h-4 w-4" />
                    <span>Abrir App</span>
                  </DropdownMenuItem>
                  <DropdownMenuItem className="cursor-pointer">
                    <Settings className="mr-2 h-4 w-4" />
                    <span>Configurações</span>
                  </DropdownMenuItem>
                  <DropdownMenuSeparator />
                  <DropdownMenuItem onClick={handleLogout} className="cursor-pointer text-red-600">
                    <LogOut className="mr-2 h-4 w-4" />
                    <span>Sair</span>
                  </DropdownMenuItem>
                </DropdownMenuContent>
              </DropdownMenu>
            ) : (
              <div className="flex items-center gap-3">
                <Link href="/login">
                  <Button variant="ghost" className="text-gray-600 hover:text-emerald-600">
                    Entrar
                  </Button>
                </Link>
                <Button onClick={onTryNow} className="bg-emerald-600 hover:bg-emerald-700 text-white">
                  Experimentar
                </Button>
              </div>
            )}
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
                Sobre
              </button>
              <button
                onClick={() => scrollToSection("how-it-works")}
                className="text-left text-gray-600 hover:text-emerald-600 transition-colors"
              >
                Como Funciona
              </button>
              <button
                onClick={() => scrollToSection("showcase")}
                className="text-left text-gray-600 hover:text-emerald-600 transition-colors"
              >
                Exemplos
              </button>
              <button
                onClick={() => scrollToSection("faq")}
                className="text-left text-gray-600 hover:text-emerald-600 transition-colors"
              >
                FAQ
              </button>

              {/* Mobile Authentication */}
              {isAuthenticated ? (
                <div className="pt-4 border-t border-gray-200 space-y-3">
                  <div className="flex items-center gap-3">
                    <Avatar className="h-8 w-8">
                      <AvatarImage src={user?.avatar || "/placeholder.svg"} alt={user?.name} />
                      <AvatarFallback className="bg-emerald-100 text-emerald-700 text-sm">
                        {user?.name ? getUserInitials(user.name) : "U"}
                      </AvatarFallback>
                    </Avatar>
                    <div>
                      <p className="text-sm font-medium">{user?.name}</p>
                      <p className="text-xs text-gray-500">{user?.email}</p>
                    </div>
                  </div>
                  <Button onClick={onTryNow} className="bg-emerald-600 hover:bg-emerald-700 text-white w-full">
                    Abrir App
                  </Button>
                  <Button
                    onClick={handleLogout}
                    variant="outline"
                    className="w-full text-red-600 border-red-200 bg-transparent"
                  >
                    Sair
                  </Button>
                </div>
              ) : (
                <div className="pt-4 border-t border-gray-200 space-y-3">
                  <Link href="/login">
                    <Button variant="outline" className="w-full bg-transparent">
                      Entrar
                    </Button>
                  </Link>
                  <Button onClick={onTryNow} className="bg-emerald-600 hover:bg-emerald-700 text-white w-full">
                    Experimentar
                  </Button>
                </div>
              )}
            </nav>
          </div>
        )}
      </div>
    </header>
  )
}
