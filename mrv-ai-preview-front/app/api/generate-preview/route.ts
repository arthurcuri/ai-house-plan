import { type NextRequest, NextResponse } from "next/server"

export async function POST(request: NextRequest) {
  try {
    const formData = await request.formData()
    const file = formData.get("floorplan") as File

    if (!file) {
      return NextResponse.json({ error: "No file provided" }, { status: 400 })
    }

    // Criar FormData para enviar para o backend Python
    const pythonBackendFormData = new FormData()
    pythonBackendFormData.append('file', file)
    
    const response = await fetch('http://127.0.0.1:8000/ocr', {
      method: 'POST',
      body: pythonBackendFormData,
    })
    
    if (!response.ok) {
      throw new Error(`Python backend failed with status: ${response.status}`)
    }
    
    // Assumindo que o backend Python retorna uma imagem
    const imageBlob = await response.blob()
    return new NextResponse(imageBlob, {
      headers: {
        'Content-Type': 'image/png',
      },
    })

    // Para demo purposes, return an error to trigger the fallback
    // return NextResponse.json({ error: "Backend not implemented yet" }, { status: 501 })
  } catch (error) {
    console.error("Error in generate-preview API:", error)
    return NextResponse.json({ error: "Internal server error" }, { status: 500 })
  }
}
