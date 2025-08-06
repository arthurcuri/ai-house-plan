import { NextRequest, NextResponse } from "next/server"
import { getApiUrl, API_CONFIG } from "@/lib/config"

export async function POST(req: NextRequest) {
  try {
    const { email, password } = await req.json()

    const response = await fetch(getApiUrl(API_CONFIG.ENDPOINTS.LOGIN), {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, senha: password }), // Backend espera 'senha'
    })

    if (!response.ok) {
      const errorData = await response.json()
      return NextResponse.json({ error: errorData.detail || "Erro ao autenticar" }, { status: response.status })
    }

    const data = await response.json()

    return NextResponse.json({
      user: {
        id: Date.now().toString(),
        name: email.split("@")[0], // Extrair nome do email como fallback
        email: email,
      },
      token: data.access_token, // Backend retorna 'access_token'
    })
  } catch (error) {
    console.error("Erro no login:", error)
    return NextResponse.json({ error: "Erro interno no servidor" }, { status: 500 })
  }
}
