"use client"

import { useState, useEffect } from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Loader2, Trash2, Palette, AlertCircle } from "lucide-react"
import { useAuth } from "@/hooks/use-auth"
import { TokenManager } from "@/lib/token-manager"
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog"

interface PersonalType {
  id: number
  nome: string
  descricao?: string
  status: "processando" | "concluido" | "erro"
  prompts_gerados: boolean
  created_at: string
  total_fotos?: number
}

export function PersonalTypeList() {
  const { user } = useAuth()
  const [tipos, setTipos] = useState<PersonalType[]>([])
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [deletingId, setDeletingId] = useState<number | null>(null)

  useEffect(() => {
    loadTipos()
  }, [])

  const loadTipos = async () => {
    setIsLoading(true)
    setError(null)

    try {
      const token = TokenManager.getToken()
      if (!token) {
        throw new Error("Você precisa estar autenticado")
      }

      const response = await fetch("/api/architect/types", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })

      if (!response.ok) {
        throw new Error(`Erro ${response.status}: ${response.statusText}`)
      }

      const data = await response.json()
      setTipos(data.tipos || [])
    } catch (err) {
      setError(err instanceof Error ? err.message : "Erro ao carregar tipos pessoais")
    } finally {
      setIsLoading(false)
    }
  }

  const handleDelete = async (id: number) => {
    setDeletingId(id)

    try {
      const token = TokenManager.getToken()
      if (!token) {
        throw new Error("Você precisa estar autenticado")
      }

      const response = await fetch(`/api/architect/types/${id}`, {
        method: "DELETE",
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })

      if (!response.ok) {
        throw new Error(`Erro ao deletar tipo`)
      }

      // Remover da lista local
      setTipos((prev) => prev.filter((t) => t.id !== id))
    } catch (err) {
      setError(err instanceof Error ? err.message : "Erro ao deletar tipo")
    } finally {
      setDeletingId(null)
    }
  }

  const getStatusBadge = (status: string) => {
    switch (status) {
      case "concluido":
        return (
          <Badge className="bg-emerald-100 text-emerald-800 border-emerald-200">
            Concluído
          </Badge>
        )
      case "processando":
        return (
          <Badge className="bg-orange-100 text-orange-800 border-orange-200">
            <Loader2 className="w-3 h-3 mr-1 animate-spin inline" />
            Processando
          </Badge>
        )
      case "erro":
        return (
          <Badge className="bg-red-100 text-red-800 border-red-200">
            Erro
          </Badge>
        )
      default:
        return null
    }
  }

  const formatDate = (dateString: string) => {
    const date = new Date(dateString)
    return date.toLocaleDateString("pt-BR", {
      day: "2-digit",
      month: "2-digit",
      year: "numeric",
      hour: "2-digit",
      minute: "2-digit",
    })
  }

  if (isLoading) {
    return (
      <div className="flex items-center justify-center py-12">
        <Loader2 className="w-8 h-8 animate-spin text-emerald-600" />
        <span className="ml-3 text-gray-600">Carregando tipos pessoais...</span>
      </div>
    )
  }

  if (error) {
    return (
      <Card className="border-red-200 bg-red-50">
        <CardContent className="pt-6">
          <div className="flex items-center gap-2 text-red-800">
            <AlertCircle className="w-5 h-5" />
            <p>{error}</p>
          </div>
          <Button
            variant="outline"
            onClick={loadTipos}
            className="mt-4"
          >
            Tentar Novamente
          </Button>
        </CardContent>
      </Card>
    )
  }

  if (tipos.length === 0) {
    return (
      <Card>
        <CardContent className="pt-6 text-center py-12">
          <Palette className="w-16 h-16 mx-auto text-gray-400 mb-4" />
          <h3 className="text-xl font-semibold text-gray-900 mb-2">
            Nenhum tipo pessoal criado ainda
          </h3>
          <p className="text-gray-600 mb-6">
            Crie seu primeiro tipo pessoal enviando fotos de seus projetos reais
          </p>
        </CardContent>
      </Card>
    )
  }

  return (
    <div className="space-y-4">
      <h2 className="text-2xl font-bold text-gray-900 mb-4">
        Meus Tipos Pessoais ({tipos.length})
      </h2>

      <div className="grid gap-4">
        {tipos.map((tipo) => (
          <Card key={tipo.id} className="hover:shadow-md transition-shadow">
            <CardHeader>
              <div className="flex items-start justify-between">
                <div className="flex-1">
                  <div className="flex items-center gap-3 mb-2">
                    <div className="w-10 h-10 bg-gradient-to-br from-emerald-500 to-emerald-600 rounded-lg flex items-center justify-center">
                      <Palette className="w-5 h-5 text-white" />
                    </div>
                    <div>
                      <CardTitle className="text-xl">{tipo.nome}</CardTitle>
                      <CardDescription className="mt-1">
                        Criado em {formatDate(tipo.created_at)}
                      </CardDescription>
                    </div>
                  </div>
                  {tipo.descricao && (
                    <p className="text-sm text-gray-600 mt-2">{tipo.descricao}</p>
                  )}
                </div>
                <div className="flex items-center gap-2">
                  {getStatusBadge(tipo.status)}
                  {tipo.status === "concluido" && tipo.prompts_gerados && (
                    <Badge variant="outline" className="text-xs">
                      Pronto para uso
                    </Badge>
                  )}
                </div>
              </div>
            </CardHeader>
            <CardContent>
              <div className="flex items-center justify-between">
                <div className="text-sm text-gray-600">
                  {tipo.total_fotos && (
                    <span>{tipo.total_fotos} fotos de referência</span>
                  )}
                </div>
                <AlertDialog>
                  <AlertDialogTrigger asChild>
                    <Button
                      variant="ghost"
                      size="sm"
                      disabled={deletingId === tipo.id}
                      className="text-red-600 hover:text-red-700 hover:bg-red-50"
                    >
                      {deletingId === tipo.id ? (
                        <Loader2 className="w-4 h-4 animate-spin" />
                      ) : (
                        <>
                          <Trash2 className="w-4 h-4 mr-2" />
                          Deletar
                        </>
                      )}
                    </Button>
                  </AlertDialogTrigger>
                  <AlertDialogContent>
                    <AlertDialogHeader>
                      <AlertDialogTitle>Confirmar exclusão</AlertDialogTitle>
                      <AlertDialogDescription>
                        Tem certeza que deseja deletar o tipo pessoal "{tipo.nome}"?
                        Esta ação não pode ser desfeita.
                      </AlertDialogDescription>
                    </AlertDialogHeader>
                    <AlertDialogFooter>
                      <AlertDialogCancel>Cancelar</AlertDialogCancel>
                      <AlertDialogAction
                        onClick={() => handleDelete(tipo.id)}
                        className="bg-red-600 hover:bg-red-700"
                      >
                        Deletar
                      </AlertDialogAction>
                    </AlertDialogFooter>
                  </AlertDialogContent>
                </AlertDialog>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  )
}


