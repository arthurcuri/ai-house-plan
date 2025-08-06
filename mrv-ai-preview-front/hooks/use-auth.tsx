"use client"

import { createContext, useContext, useState, useEffect, type ReactNode } from "react"
import { toast } from "@/components/ui/use-toast"
import { TokenManager } from "@/lib/token-manager"

interface User {
  id: string
  name: string
  email: string
}

interface AuthContextType {
  user: User | null
  isAuthenticated: boolean
  isLoading: boolean
  login: (email: string, password: string) => Promise<void>
  register: (name: string, email: string, password: string) => Promise<void>
  logout: () => void
  validateSession: () => Promise<boolean>
}

const AuthContext = createContext<AuthContextType | undefined>(undefined)

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null)
  const [isAuthenticated, setIsAuthenticated] = useState(false)
  const [isLoading, setIsLoading] = useState(true)

  const validateSession = async (): Promise<boolean> => {
    const token = TokenManager.getToken()
    if (!token) return false

    // Verificar se o token expirou localmente
    if (TokenManager.isTokenExpired(token)) {
      logout()
      return false
    }

    // Validar com o servidor (opcional - pode ser pesado)
    try {
      const isValid = await TokenManager.validateTokenWithServer()
      if (!isValid) {
        logout()
        return false
      }
      return true
    } catch {
      // Se falhar a validação com servidor, manter sessão local se token não expirou
      return true
    }
  }

  useEffect(() => {
    const initAuth = async () => {
      const savedUser = localStorage.getItem("mrv-user")
      const token = TokenManager.getToken()
      
      if (savedUser && token) {
        // Verificar se token não expirou
        if (!TokenManager.isTokenExpired(token)) {
          const userData = JSON.parse(savedUser)
          setUser(userData)
          setIsAuthenticated(true)
        } else {
          // Token expirado, limpar dados
          TokenManager.removeToken()
        }
      }
      setIsLoading(false)
    }

    initAuth()
  }, [])

  const login = async (email: string, password: string) => {
    try {
      const response = await fetch("/api/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password }),
      })

      if (!response.ok) {
        const errorData = await response.json()
        throw new Error(errorData.error || "Credenciais inválidas")
      }

      const data = await response.json()
      const userData: User = {
        id: data.user?.id || Date.now().toString(),
        name: data.user?.name || email.split("@")[0],
        email,
      }

      setUser(userData)
      setIsAuthenticated(true)
      localStorage.setItem("mrv-user", JSON.stringify(userData))
      TokenManager.setToken(data.token)
      toast({ title: "Login realizado com sucesso" })
    } catch (error: any) {
      toast({ title: "Erro ao fazer login", description: error.message, variant: "destructive" })
      throw error
    }
  }

  const register = async (name: string, email: string, password: string) => {
    try {
      const response = await fetch("/api/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ name, email, password }),
      })

      if (!response.ok) {
        const errorData = await response.json()
        throw new Error(errorData.error || "Erro ao registrar")
      }

      const data = await response.json()
      const userData: User = {
        id: data.user?.id || Date.now().toString(),
        name: data.user?.name || name,
        email,
      }

      setUser(userData)
      setIsAuthenticated(true)
      localStorage.setItem("mrv-user", JSON.stringify(userData))
      TokenManager.setToken(data.token)
      toast({ title: "Conta criada com sucesso" })
    } catch (error: any) {
      toast({ title: "Erro ao registrar", description: error.message, variant: "destructive" })
      throw error
    }
  }

  const logout = () => {
    setUser(null)
    setIsAuthenticated(false)
    TokenManager.removeToken()
    toast({ title: "Logout realizado com sucesso" })
  }

  return (
    <AuthContext.Provider value={{ user, isAuthenticated, isLoading, login, register, logout, validateSession }}>
      {children}
    </AuthContext.Provider>
  )
}

export function useAuth() {
  const context = useContext(AuthContext)
  if (context === undefined) {
    throw new Error("useAuth must be used within an AuthProvider")
  }
  return context
}
