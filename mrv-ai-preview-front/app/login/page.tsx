// File: app/login/page.tsx
"use client"

import type React from "react"
import { useState, useEffect } from "react"
import { useRouter, useSearchParams } from "next/navigation"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Eye, EyeOff, Building2, Mail, Lock, ArrowLeft } from "lucide-react"
import { useAuth } from "@/hooks/use-auth"
import Link from "next/link"

export default function LoginPage() {
  const [showPassword, setShowPassword] = useState(false)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState("")
  const { login } = useAuth()
  const router = useRouter()
  const searchParams = useSearchParams()

  const [loginForm, setLoginForm] = useState({
    email: "",
    password: "",
  })

  // Verificar se há parâmetros de redirecionamento
  const redirectUrl = searchParams.get('redirect')
  const action = searchParams.get('action')

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsLoading(true)
    setError("")

    // Validações básicas
    if (!loginForm.email.trim() || !loginForm.password.trim()) {
      setError("Email e senha são obrigatórios")
      setIsLoading(false)
      return
    }

    if (!loginForm.email.includes("@") || !loginForm.email.includes(".")) {
      setError("Email inválido")
      setIsLoading(false)
      return
    }

    try {
      await login(loginForm.email.toLowerCase().trim(), loginForm.password)
      
      // Redirecionar baseado nos parâmetros
      if (redirectUrl && action === 'start-app') {
        router.push("/?start-app=true")
      } else if (redirectUrl) {
        window.location.href = redirectUrl
      } else {
        router.push("/")
      }
    } catch (error) {
      setError("Email ou senha incorretos. Tente novamente.")
      console.error("Login failed:", error)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-emerald-50 via-white to-orange-50 flex items-center justify-center p-4">
      <div className="w-full max-w-md">
        {/* Back to Home */}
        <div className="mb-6">
          <Link href="/">
            <Button variant="ghost" className="text-gray-600 hover:text-emerald-600 p-0">
              <ArrowLeft className="w-4 h-4 mr-2" />
              Voltar ao início
            </Button>
          </Link>
        </div>

        <Card className="shadow-2xl border-0">
          <CardHeader className="bg-gradient-to-br from-emerald-600 to-emerald-700 text-white rounded-t-lg">
            <div className="flex items-center gap-3 mb-4">
              <div className="flex items-center gap-2">
                <div className="w-8 h-8 bg-white/20 rounded-lg flex items-center justify-center">
                  <Building2 className="w-5 h-5 text-white" />
                </div>
                <div className="w-8 h-8 bg-gradient-to-br from-orange-500 to-orange-600 rounded-lg flex items-center justify-center transform rotate-45">
                  <div className="w-3 h-3 bg-white rounded-sm transform -rotate-45" />
                </div>
              </div>
              <span className="text-xl font-bold">House AI Preview</span>
            </div>
            <CardTitle className="text-2xl">Bem-vindo de volta</CardTitle>
            <p className="text-emerald-100">Faça login para acessar suas visualizações de apartamentos com IA</p>
          </CardHeader>

          <CardContent className="p-8">
            {error && (
              <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">
                {error}
              </div>
            )}

            <form onSubmit={handleLogin} className="space-y-6">
              <div className="space-y-2">
                <Label htmlFor="email">Email</Label>
                <div className="relative">
                  <Mail className="absolute left-3 top-3 h-4 w-4 text-gray-400" />
                  <Input
                    id="email"
                    type="email"
                    placeholder="Digite seu email"
                    value={loginForm.email}
                    onChange={(e) => setLoginForm({ ...loginForm, email: e.target.value })}
                    className="pl-10"
                    required
                  />
                </div>
              </div>

              <div className="space-y-2">
                <Label htmlFor="password">Senha</Label>
                <div className="relative">
                  <Lock className="absolute left-3 top-3 h-4 w-4 text-gray-400" />
                  <Input
                    id="password"
                    type={showPassword ? "text" : "password"}
                    placeholder="Digite sua senha"
                    value={loginForm.password}
                    onChange={(e) => setLoginForm({ ...loginForm, password: e.target.value })}
                    className="pl-10 pr-10"
                    required
                  />
                  <button
                    type="button"
                    onClick={() => setShowPassword(!showPassword)}
                    className="absolute right-3 top-3 text-gray-400 hover:text-gray-600"
                  >
                    {showPassword ? <EyeOff className="h-4 w-4" /> : <Eye className="h-4 w-4" />}
                  </button>
                </div>
              </div>

              <Button
                type="submit"
                className="w-full bg-emerald-600 hover:bg-emerald-700 text-white py-3"
                disabled={isLoading}
              >
                {isLoading ? "Entrando..." : "Entrar"}
              </Button>
            </form>

            <div className="mt-6 text-center">
              <Link href="/forgot-password">
                <button className="text-sm text-emerald-600 hover:text-emerald-700">Esqueceu sua senha?</button>
              </Link>
            </div>

            <div className="mt-6 text-center">
              <p className="text-gray-600">
                Não tem uma conta?{' '}
                <Link href="/register" className="text-emerald-600 hover:text-emerald-700 font-medium">
                  Criar conta
                </Link>
              </p>
            </div>

            <div className="mt-6 text-center text-sm text-gray-500">
              Ao continuar, você concorda com nossos{' '}
              <a href="#" className="text-emerald-600 hover:text-emerald-700">Termos de Serviço</a>{' '}
              e{' '}
              <a href="#" className="text-emerald-600 hover:text-emerald-700">Política de Privacidade</a>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}