"use client"

import type React from "react"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Mail, ArrowLeft, CheckCircle } from "lucide-react"
import { Building2 } from "lucide-react"
import Link from "next/link"

export default function ForgotPasswordPage() {
  const [email, setEmail] = useState("")
  const [isLoading, setIsLoading] = useState(false)
  const [isEmailSent, setIsEmailSent] = useState(false)
  const [error, setError] = useState("")

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsLoading(true)
    setError("")

    try {
      // Simulate API call for password reset
      await new Promise((resolve) => setTimeout(resolve, 2000))

      // In a real app, you would call your password reset API here
      // const response = await fetch('/api/forgot-password', {
      //   method: 'POST',
      //   headers: { 'Content-Type': 'application/json' },
      //   body: JSON.stringify({ email })
      // })

      setIsEmailSent(true)
    } catch (error) {
      setError("Erro ao enviar email de recuperação. Tente novamente.")
      console.error("Password reset failed:", error)
    } finally {
      setIsLoading(false)
    }
  }

  if (isEmailSent) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-emerald-50 via-white to-orange-50 flex items-center justify-center p-4">
        <div className="w-full max-w-md">
          <div className="mb-6">
            <Link href="/login">
              <Button variant="ghost" className="text-gray-600 hover:text-emerald-600 p-0">
                <ArrowLeft className="w-4 h-4 mr-2" />
                Voltar ao login
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
                <span className="text-xl font-bold">MRV AI Preview</span>
              </div>
              <CardTitle className="text-2xl">Email Enviado!</CardTitle>
              <p className="text-emerald-100">Verifique sua caixa de entrada para redefinir sua senha</p>
            </CardHeader>

            <CardContent className="p-8 text-center">
              <div className="mb-6">
                <div className="w-16 h-16 bg-emerald-100 rounded-full flex items-center justify-center mx-auto mb-4">
                  <CheckCircle className="w-8 h-8 text-emerald-600" />
                </div>
                <h3 className="text-lg font-semibold text-gray-900 mb-2">Verifique seu email</h3>
                <p className="text-gray-600 mb-4">Enviamos um link de recuperação de senha para:</p>
                <p className="font-medium text-gray-900 bg-gray-50 px-4 py-2 rounded-lg">{email}</p>
              </div>

              <div className="space-y-4">
                <p className="text-sm text-gray-600">
                  Não recebeu o email? Verifique sua pasta de spam ou tente novamente.
                </p>

                <Button
                  onClick={() => {
                    setIsEmailSent(false)
                    setEmail("")
                  }}
                  variant="outline"
                  className="w-full bg-transparent"
                >
                  Tentar outro email
                </Button>

                <Link href="/login">
                  <Button className="w-full bg-emerald-600 hover:bg-emerald-700 text-white">Voltar ao Login</Button>
                </Link>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-emerald-50 via-white to-orange-50 flex items-center justify-center p-4">
      <div className="w-full max-w-md">
        {/* Back to Login */}
        <div className="mb-6">
          <Link href="/login">
            <Button variant="ghost" className="text-gray-600 hover:text-emerald-600 p-0">
              <ArrowLeft className="w-4 h-4 mr-2" />
              Voltar ao login
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
              <span className="text-xl font-bold">MRV AI Preview</span>
            </div>
            <CardTitle className="text-2xl">Esqueceu sua senha?</CardTitle>
            <p className="text-emerald-100">Digite seu email e enviaremos um link para redefinir sua senha</p>
          </CardHeader>

          <CardContent className="p-8">
            {error && (
              <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">{error}</div>
            )}

            <form onSubmit={handleSubmit} className="space-y-6">
              <div className="space-y-2">
                <Label htmlFor="email">Email</Label>
                <div className="relative">
                  <Mail className="absolute left-3 top-3 h-4 w-4 text-gray-400" />
                  <Input
                    id="email"
                    type="email"
                    placeholder="Digite seu email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    className="pl-10"
                    required
                  />
                </div>
              </div>

              <Button
                type="submit"
                className="w-full bg-emerald-600 hover:bg-emerald-700 text-white py-3"
                disabled={isLoading}
              >
                {isLoading ? "Enviando..." : "Enviar Link de Recuperação"}
              </Button>
            </form>

            <div className="mt-6 text-center">
              <p className="text-gray-600">
                Lembrou da senha?{" "}
                <Link href="/login" className="text-emerald-600 hover:text-emerald-700 font-medium">
                  Fazer login
                </Link>
              </p>
            </div>

            <div className="mt-6 text-center text-sm text-gray-500">
              Ao continuar, você concorda com nossos{" "}
              <a href="#" className="text-emerald-600 hover:text-emerald-700">
                Termos de Serviço
              </a>{" "}
              e{" "}
              <a href="#" className="text-emerald-600 hover:text-emerald-700">
                Política de Privacidade
              </a>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
