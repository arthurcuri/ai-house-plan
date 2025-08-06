import { NextRequest, NextResponse } from "next/server"
import { getApiUrl, API_CONFIG } from "@/lib/config"

export async function POST(req: NextRequest) {
  try {
    const authHeader = req.headers.get('authorization')
    
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return NextResponse.json({ error: "Token não fornecido" }, { status: 401 })
    }

    const token = authHeader.substring(7)

    const response = await fetch(`${getApiUrl('')}/auth/validate-token`, {
      method: "POST",
      headers: { 
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
      },
    })

    if (!response.ok) {
      const errorData = await response.json()
      return NextResponse.json({ error: errorData.detail || "Token inválido" }, { status: response.status })
    }

    const data = await response.json()
    return NextResponse.json(data)
    
  } catch (error) {
    console.error("Erro na validação do token:", error)
    return NextResponse.json({ error: "Erro interno no servidor" }, { status: 500 })
  }
}
