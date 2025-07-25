import { type NextRequest, NextResponse } from "next/server"

export async function POST(request: NextRequest) {
  try {
    const formData = await request.formData()
    const file = formData.get("floorplan") as File
    const category = formData.get("category") as string

    if (!file) {
      return NextResponse.json({ error: "No file provided" }, { status: 400 })
    }

    if (!category) {
      return NextResponse.json({ error: "No category provided" }, { status: 400 })
    }

    // Criar FormData para enviar para o backend Python
    const pythonBackendFormData = new FormData()
    pythonBackendFormData.append('file', file)
    pythonBackendFormData.append('tipo', category) // Enviar categoria como "tipo"
    
    const response = await fetch('http://127.0.0.1:8000/ocr', {
      method: 'POST',
      body: pythonBackendFormData,
    })
    
    if (!response.ok) {
      throw new Error(`Python backend failed with status: ${response.status}`)
    }
    
    // ✅ ATUALIZADO: Agora o backend retorna JSON com interpretacao_llm
    const jsonResponse = await response.json()
    
    return NextResponse.json({
      success: true,
      data: jsonResponse
    })

  } catch (error) {
    console.error("Error in generate-preview API:", error)
    return NextResponse.json({ error: "Internal server error" }, { status: 500 })
  }
}
