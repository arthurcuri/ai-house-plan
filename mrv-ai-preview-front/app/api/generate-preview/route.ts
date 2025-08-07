import { type NextRequest, NextResponse } from "next/server"

export async function POST(request: NextRequest) {
  try {
    const formData = await request.formData()
    const file = formData.get("floorplan") as File
    const category = formData.get("category") as string
    const generateImages = formData.get("generateImages") as string // Novo parâmetro
    const authToken = formData.get("authToken") as string // Token de autenticação

    if (!file) {
      return NextResponse.json({ error: "No file provided" }, { status: 400 })
    }

    if (!category) {
      return NextResponse.json({ error: "No category provided" }, { status: 400 })
    }

    // Decidir qual endpoint usar baseado no parâmetro generateImages
    const shouldGenerateImages = generateImages === "true"
    
    let endpoint: string
    let headers: Record<string, string> = {}
    
    if (shouldGenerateImages) {
      if (!authToken) {
        return NextResponse.json({ error: "Authentication token required for image generation" }, { status: 401 })
      }
      endpoint = 'http://127.0.0.1:8000/gerar-imagens-hd'  // Rota com autenticação
      headers['Authorization'] = `Bearer ${authToken}`
    } else {
      endpoint = 'http://127.0.0.1:8000/ocr'  // Para apenas OCR + interpretação
    }

    // Criar FormData para enviar para o backend Python
    const pythonBackendFormData = new FormData()
    pythonBackendFormData.append('file', file)
    pythonBackendFormData.append('tipo', category) // Enviar categoria como "tipo"
    
    const response = await fetch(endpoint, {
      method: 'POST',
      headers: headers,
      body: pythonBackendFormData,
    })
    
    if (!response.ok) {
      if (response.status === 401) {
        return NextResponse.json({ error: "Authentication failed" }, { status: 401 })
      }
      throw new Error(`Python backend failed with status: ${response.status}`)
    }
    
    const jsonResponse = await response.json()
    
    return NextResponse.json({
      success: true,
      data: jsonResponse,
      mode: shouldGenerateImages ? 'images' : 'preview'
    })

  } catch (error) {
    console.error("Error in generate-preview API:", error)
    return NextResponse.json({ error: "Internal server error" }, { status: 500 })
  }
}
