import { type NextRequest, NextResponse } from "next/server"

const BACKEND_URL = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000"

export async function GET(request: NextRequest) {
  try {
    const authHeader = request.headers.get("authorization")
    
    if (!authHeader) {
      return NextResponse.json(
        { error: "Token de autenticação não fornecido" },
        { status: 401 }
      )
    }

    // Log do token recebido (apenas preview por segurança)
    const tokenPreview = authHeader.substring(0, 20) + "..."
    console.log(`[DEBUG] GET - Token recebido: ${tokenPreview}`)

    const response = await fetch(`${BACKEND_URL}/arquiteto/tipos`, {
      method: "GET",
      headers: {
        Authorization: authHeader,
        "Content-Type": "application/json",
      },
    })

    if (!response.ok) {
      const errorText = await response.text()
      return NextResponse.json(
        { error: errorText || `Erro ${response.status}` },
        { status: response.status }
      )
    }

    const data = await response.json()
    return NextResponse.json(data)
  } catch (error) {
    console.error("Erro ao buscar tipos pessoais:", error)
    return NextResponse.json(
      { error: "Erro ao comunicar com o backend" },
      { status: 500 }
    )
  }
}

export async function POST(request: NextRequest) {
  try {
    const authHeader = request.headers.get("authorization")
    
    if (!authHeader) {
      return NextResponse.json(
        { error: "Token de autenticação não fornecido" },
        { status: 401 }
      )
    }

    // Log do token recebido (apenas preview por segurança)
    const tokenPreview = authHeader.substring(0, 20) + "..."
    console.log(`[DEBUG] Token recebido na rota /api/architect/types: ${tokenPreview}`)
    console.log(`[DEBUG] Token completo length: ${authHeader.length}`)

    // Obter FormData da requisição
    const formData = await request.formData()

    // Reenviar para o backend Python
    console.log(`[DEBUG] Enviando requisição para: ${BACKEND_URL}/arquiteto/tipos`)
    const response = await fetch(`${BACKEND_URL}/arquiteto/tipos`, {
      method: "POST",
      headers: {
        Authorization: authHeader,
      },
      body: formData,
    })

    console.log(`[DEBUG] Resposta do backend: ${response.status} ${response.statusText}`)

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({ error: "Erro desconhecido" }))
      console.error(`[DEBUG] Erro do backend:`, errorData)
      return NextResponse.json(
        { error: errorData.error || `Erro ${response.status}` },
        { status: response.status }
      )
    }

    const data = await response.json()
    return NextResponse.json(data)
  } catch (error) {
    console.error("Erro ao criar tipo pessoal:", error)
    return NextResponse.json(
      { error: "Erro ao comunicar com o backend" },
      { status: 500 }
    )
  }
}



