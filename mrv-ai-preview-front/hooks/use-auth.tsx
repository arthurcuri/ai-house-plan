"use client"

import { createContext, useContext, useState, useEffect, type ReactNode } from "react"
import { toast } from "@/components/ui/use-toast"

interface User {
  id: string
  name: string
  email: string
  avatar?: string
}

interface AuthContextType {
  user: User | null
  isAuthenticated: boolean
  login: (email: string, password: string) => Promise<void>
  register: (name: string, email: string, password: string) => Promise<void>
  logout: () => void
}

const AuthContext = createContext<AuthContextType | undefined>(undefined)

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null)
  const [isAuthenticated, setIsAuthenticated] = useState(false)

  useEffect(() => {
    const savedUser = localStorage.getItem("mrv-user")
    const token = localStorage.getItem("mrv-token")
    if (savedUser && token) {
      const userData = JSON.parse(savedUser)
      setUser(userData)
      setIsAuthenticated(true)
    }
  }, [])

  const login = async (email: string, password: string) => {
    try {
      const response = await fetch("http://127.0.0.1:8000/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, senha: password }),
      })

      if (!response.ok) throw new Error("Credenciais inválidas")

      const data = await response.json()
      const userData: User = {
        id: Date.now().toString(),
        name: email.split("@")[0],
        email,
        avatar: `https://api.dicebear.com/7.x/avataaars/svg?seed=${email}`,
      }

      setUser(userData)
      setIsAuthenticated(true)
      localStorage.setItem("mrv-user", JSON.stringify(userData))
      localStorage.setItem("mrv-token", data.access_token)
      toast({ title: "Login realizado com sucesso" })
    } catch (error: any) {
      toast({ title: "Erro ao fazer login", description: error.message, variant: "destructive" })
      throw error
    }
  }

  const register = async (name: string, email: string, password: string) => {
    try {
      const body = JSON.stringify({ nome: name, email, senha: password })

      const response = await fetch("http://127.0.0.1:8000/auth/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body,
      })

      if (!response.ok) throw new Error("Erro ao registrar")

      const data = await response.json()
      const userData: User = {
        id: Date.now().toString(),
        name,
        email,
        avatar: `https://api.dicebear.com/7.x/avataaars/svg?seed=${email}`,
      }

      setUser(userData)
      setIsAuthenticated(true)
      localStorage.setItem("mrv-user", JSON.stringify(userData))
      localStorage.setItem("mrv-token", data.access_token)
      toast({ title: "Conta criada com sucesso" })
    } catch (error: any) {
      toast({ title: "Erro ao registrar", description: error.message, variant: "destructive" })
      throw error
    }
  }

  const logout = () => {
    setUser(null)
    setIsAuthenticated(false)
    localStorage.removeItem("mrv-user")
    localStorage.removeItem("mrv-token")
    toast({ title: "Logout realizado com sucesso" })
  }

  return (
    <AuthContext.Provider value={{ user, isAuthenticated, login, register, logout }}>
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
