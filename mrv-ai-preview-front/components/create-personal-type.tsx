"use client"

import { useState, useRef } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { X, Upload, Loader2, AlertCircle, CheckCircle2 } from "lucide-react"
import { Alert, AlertDescription } from "@/components/ui/alert"
import { useAuth } from "@/hooks/use-auth"
import { TokenManager } from "@/lib/token-manager"

interface CreatePersonalTypeProps {
  onCancel: () => void
  onSuccess: () => void
}

interface UploadedPhoto {
  file: File
  preview: string
  id: string
}

export function CreatePersonalType({ onCancel, onSuccess }: CreatePersonalTypeProps) {
  const { user } = useAuth()
  const [nome, setNome] = useState("")
  const [fotos, setFotos] = useState<UploadedPhoto[]>([])
  const [isProcessing, setIsProcessing] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [success, setSuccess] = useState(false)
  const fileInputRef = useRef<HTMLInputElement>(null)

  const MAX_PHOTOS = 20
  const MIN_PHOTOS = 10
  const MAX_FILE_SIZE = 10 * 1024 * 1024 // 10MB

  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const files = Array.from(e.target.files || [])
    
    if (fotos.length + files.length > MAX_PHOTOS) {
      setError(`Você pode enviar no máximo ${MAX_PHOTOS} fotos`)
      return
    }

    const validFiles = files.filter((file) => {
      if (!file.type.startsWith("image/")) {
        setError(`${file.name} não é uma imagem válida`)
        return false
      }
      if (file.size > MAX_FILE_SIZE) {
        setError(`${file.name} é muito grande (máximo 10MB)`)
        return false
      }
      return true
    })

    const newPhotos: UploadedPhoto[] = validFiles.map((file) => ({
      file,
      preview: URL.createObjectURL(file),
      id: Math.random().toString(36).substring(7),
    }))

    setFotos((prev) => [...prev, ...newPhotos])
    setError(null)
  }

  const removePhoto = (id: string) => {
    setFotos((prev) => {
      const photo = prev.find((p) => p.id === id)
      if (photo) {
        URL.revokeObjectURL(photo.preview)
      }
      return prev.filter((p) => p.id !== id)
    })
  }

  const handleSubmit = async () => {
    setError(null)
    setSuccess(false)

    // Validações
    if (!nome.trim()) {
      setError("Por favor, informe um nome para o tipo")
      return
    }

    if (fotos.length < MIN_PHOTOS) {
      setError(`Você precisa enviar pelo menos ${MIN_PHOTOS} fotos`)
      return
    }

    if (fotos.length > MAX_PHOTOS) {
      setError(`Você pode enviar no máximo ${MAX_PHOTOS} fotos`)
      return
    }

    setIsProcessing(true)

    try {
      const token = TokenManager.getToken()
      if (!token) {
        throw new Error("Você precisa estar autenticado")
      }

      const formData = new FormData()
      formData.append("nome", nome.trim())
      fotos.forEach((photo) => {
        formData.append("fotos", photo.file)
      })

      const response = await fetch("/api/architect/types", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
        },
        body: formData,
      })

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({ error: "Erro desconhecido" }))
        throw new Error(errorData.error || `Erro ${response.status}: ${response.statusText}`)
      }

      const data = await response.json()
      setSuccess(true)
      
      // Limpar formulário
      setNome("")
      setFotos.forEach((photo) => URL.revokeObjectURL(photo.preview))
      setFotos([])
      
      // Chamar callback de sucesso após um breve delay
      setTimeout(() => {
        onSuccess()
      }, 1500)
    } catch (err) {
      setError(err instanceof Error ? err.message : "Erro ao criar tipo pessoal")
    } finally {
      setIsProcessing(false)
    }
  }

  return (
    <Card className="border-2">
      <CardHeader>
        <CardTitle className="text-2xl">Criar Novo Tipo Pessoal</CardTitle>
        <CardDescription>
          Envie fotos de seus projetos reais para criar um estilo arquitetônico personalizado
        </CardDescription>
      </CardHeader>
      <CardContent className="space-y-6">
        {/* Nome do Tipo */}
        <div className="space-y-2">
          <Label htmlFor="nome">Nome do Tipo *</Label>
          <Input
            id="nome"
            value={nome}
            onChange={(e) => setNome(e.target.value)}
            placeholder="Ex: Minimalista Moderno, Industrial Chic, etc."
            disabled={isProcessing}
            className="max-w-md"
          />
        </div>

        {/* Upload de Fotos */}
        <div className="space-y-2">
          <Label>Fotos de Referência *</Label>
          <div className="border-2 border-dashed border-gray-300 rounded-lg p-6 text-center hover:border-emerald-500 transition-colors">
            <input
              ref={fileInputRef}
              type="file"
              multiple
              accept="image/*"
              onChange={handleFileSelect}
              disabled={isProcessing || fotos.length >= MAX_PHOTOS}
              className="hidden"
            />
            <Upload className="w-12 h-12 mx-auto text-gray-400 mb-4" />
            <p className="text-gray-600 mb-2">
              Clique para selecionar ou arraste fotos aqui
            </p>
            <p className="text-sm text-gray-500">
              {MIN_PHOTOS}-{MAX_PHOTOS} fotos • Máximo 10MB por foto
            </p>
            <Button
              type="button"
              variant="outline"
              onClick={() => fileInputRef.current?.click()}
              disabled={isProcessing || fotos.length >= MAX_PHOTOS}
              className="mt-4"
            >
              Selecionar Fotos
            </Button>
          </div>

          {/* Contador de Fotos */}
          <div className="text-sm text-gray-600">
            {fotos.length} / {MAX_PHOTOS} fotos selecionadas
            {fotos.length < MIN_PHOTOS && (
              <span className="text-orange-600 ml-2">
                (mínimo {MIN_PHOTOS} fotos)
              </span>
            )}
          </div>
        </div>

        {/* Preview das Fotos */}
        {fotos.length > 0 && (
          <div className="space-y-2">
            <Label>Fotos Selecionadas</Label>
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
              {fotos.map((photo) => (
                <div key={photo.id} className="relative group">
                  <img
                    src={photo.preview}
                    alt="Preview"
                    className="w-full h-32 object-cover rounded-lg border border-gray-200"
                  />
                  <button
                    type="button"
                    onClick={() => removePhoto(photo.id)}
                    disabled={isProcessing}
                    className="absolute top-2 right-2 bg-red-500 text-white rounded-full p-1 opacity-0 group-hover:opacity-100 transition-opacity hover:bg-red-600"
                  >
                    <X className="w-4 h-4" />
                  </button>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Mensagens de Erro/Sucesso */}
        {error && (
          <Alert variant="destructive">
            <AlertCircle className="h-4 w-4" />
            <AlertDescription>{error}</AlertDescription>
          </Alert>
        )}

        {success && (
          <Alert className="border-emerald-500 bg-emerald-50">
            <CheckCircle2 className="h-4 w-4 text-emerald-600" />
            <AlertDescription className="text-emerald-800">
              Tipo pessoal criado com sucesso! Analisando fotos...
            </AlertDescription>
          </Alert>
        )}

        {/* Botões de Ação */}
        <div className="flex gap-4 pt-4">
          <Button
            onClick={handleSubmit}
            disabled={isProcessing || !nome.trim() || fotos.length < MIN_PHOTOS}
            className="bg-emerald-600 hover:bg-emerald-700 text-white flex-1"
          >
            {isProcessing ? (
              <>
                <Loader2 className="w-4 h-4 mr-2 animate-spin" />
                Processando...
              </>
            ) : (
              "Criar Tipo"
            )}
          </Button>
          <Button
            variant="outline"
            onClick={onCancel}
            disabled={isProcessing}
          >
            Cancelar
          </Button>
        </div>
      </CardContent>
    </Card>
  )
}


