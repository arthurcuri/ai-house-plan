import { type NextRequest, NextResponse } from "next/server"

const BACKEND_URL = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000"

export async function DELETE(
  request: NextRequest,
  { params }: { params: { id: string } }
) {
  try {
    const authHeader = request.headers.get("authorization")
    
    if (!authHeader) {
      return NextResponse.json(
        { error: "Token de autenticação não fornecido" },
        { status: 401 }
      )
    }

    const { id } = params

    const response = await fetch(`${BACKEND_URL}/arquiteto/tipos/${id}`, {
      method: "DELETE",
      headers: {
        Authorization: authHeader,
        "Content-Type": "application/json",
      },
    })

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({ error: "Erro desconhecido" }))
      return NextResponse.json(
        { error: errorData.error || `Erro ${response.status}` },
        { status: response.status }
      )
    }

    return NextResponse.json({ success: true })
  } catch (error) {
    console.error("Erro ao deletar tipo pessoal:", error)
    return NextResponse.json(
      { error: "Erro ao comunicar com o backend" },
      { status: 500 }
    )
  }
}



