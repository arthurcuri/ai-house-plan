"use client"

import { useState, useEffect } from "react"
import { useRouter } from "next/navigation"
import { Button } from "@/components/ui/button"
import { ArrowLeft, Plus, Palette } from "lucide-react"
import { useAuth } from "@/hooks/use-auth"
import { CreatePersonalType } from "@/components/create-personal-type"
import { PersonalTypeList } from "@/components/personal-type-list"
import { Header } from "@/components/header"

export default function ArquitetoPage() {
  const router = useRouter()
  const { isAuthenticated, isLoading } = useAuth()
  const [showCreateForm, setShowCreateForm] = useState(false)
  const [refreshKey, setRefreshKey] = useState(0)

  useEffect(() => {
    if (!isLoading && !isAuthenticated) {
      router.push("/login?redirect=/arquiteto")
    }
  }, [isAuthenticated, isLoading, router])

  const handleTypeCreated = () => {
    setShowCreateForm(false)
    setRefreshKey((prev) => prev + 1)
  }

  if (isLoading) {
    return (
      <div className="min-h-screen bg-white flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-emerald-600 mx-auto"></div>
          <p className="mt-4 text-gray-600">Carregando...</p>
        </div>
      </div>
    )
  }

  if (!isAuthenticated) {
    return null
  }

  return (
    <div className="min-h-screen bg-white">
      <Header />
      
      <main className="container mx-auto px-4 py-8 max-w-6xl">
        {/* Header da Página */}
        <div className="mb-8">
          <Button
            variant="ghost"
            onClick={() => router.push("/features")}
            className="mb-4 text-gray-600 hover:text-emerald-600"
          >
            <ArrowLeft className="w-4 h-4 mr-2" />
            Voltar
          </Button>

          <div className="flex items-center justify-between">
            <div className="flex items-center gap-4">
              <div className="w-12 h-12 bg-gradient-to-br from-emerald-500 to-emerald-600 rounded-lg flex items-center justify-center">
                <Palette className="w-6 h-6 text-white" />
              </div>
              <div>
                <h1 className="text-3xl font-bold text-gray-900">Área do Arquiteto</h1>
                <p className="text-gray-600 mt-1">
                  Crie e gerencie seus tipos pessoais de arquitetura
                </p>
              </div>
            </div>

            {!showCreateForm && (
              <Button
                onClick={() => setShowCreateForm(true)}
                className="bg-emerald-600 hover:bg-emerald-700 text-white"
              >
                <Plus className="w-4 h-4 mr-2" />
                Criar Novo Tipo
              </Button>
            )}
          </div>
        </div>

        {/* Formulário de Criação */}
        {showCreateForm && (
          <div className="mb-8">
            <CreatePersonalType
              onCancel={() => setShowCreateForm(false)}
              onSuccess={handleTypeCreated}
            />
          </div>
        )}

        {/* Lista de Tipos Pessoais */}
        <PersonalTypeList key={refreshKey} />
      </main>
    </div>
  )
}

