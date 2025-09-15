import { type NextRequest, NextResponse } from "next/server"

export async function POST(request: NextRequest) {
  try {
    const formData = await request.formData()
    const file = formData.get("floorplan") as File
    const category = formData.get("category") as string
    const authToken = formData.get("authToken") as string || 'dummy-token'

    if (!file) {
      return NextResponse.json({ error: "No file provided" }, { status: 400 })
    }

    if (!category) {
      return NextResponse.json({ error: "No category provided" }, { status: 400 })
    }

    // Sempre gerar imagens quando o botão Generate Preview for clicado
    const endpoint = 'http://127.0.0.1:8000/gerar-imagens'
    const headers: Record<string, string> = {
      'Authorization': `Bearer ${authToken}`
    }

    // Criar FormData para enviar para o backend Python
    const pythonBackendFormData = new FormData()
    pythonBackendFormData.append('file', file)
    pythonBackendFormData.append('tipo', category)
    
    console.log(`Sending request to: ${endpoint}`)
    console.log(`Category: ${category}`)
    
    const response = await fetch(endpoint, {
      method: 'POST',
      headers: headers,
      body: pythonBackendFormData,
    })
    
    if (!response.ok) {
      const errorText = await response.text()
      console.error(`Python backend error: ${errorText}`)
      return NextResponse.json({ 
        error: "Backend request failed", 
        details: errorText,
        status: response.status 
      }, { status: response.status })
    }
    
    const jsonResponse = await response.json()
    console.log('Backend response:', jsonResponse)
    
    // Processar as imagens geradas da pasta generated_images
    const images = jsonResponse.resultado || jsonResponse.imagens || jsonResponse.images || []
    
    console.log('Processing images:', images.length, 'images found')
    
    if (images.length === 0) {
      return NextResponse.json({
        success: true,
        data: {
          images: [],
          metadata: {
            category,
            totalImages: 0,
            generatedAt: new Date().toISOString(),
            message: "No images generated"
          }
        },
        mode: 'images'
      })
    }

    const processedImages = images.map((img: any, index: number) => {
      let imageUrl = null
      
      // Usar a url_relativa do backend para construir URL do Next.js
      if (img.url_relativa) {
        // Converter /imagens/folder/file.png para /api/images/folder/file.png
        const relativePath = img.url_relativa.replace('/imagens/', '')
        imageUrl = `/api/images/${relativePath}`
        console.log(`Image ${index}: ${img.comodo} -> ${imageUrl}`)
      } else if (img.arquivo || img.caminho || img.path) {
        // Fallback: extrair pasta e arquivo do caminho completo
        const fullPath = img.arquivo || img.caminho || img.path
        const pathParts = fullPath.split('/')
        const folderAndFile = pathParts.slice(-2).join('/') // pega pasta/arquivo.png
        imageUrl = `/api/images/${folderAndFile}`
        console.log(`Image ${index}: Using file path -> ${imageUrl}`)
      } else if (img.url) {
        imageUrl = img.url
      } else if (img.base64) {
        const base64Data = img.base64.startsWith('data:') ? img.base64 : `data:image/jpeg;base64,${img.base64}`
        imageUrl = base64Data
      } else if (img.imagem) {
        imageUrl = img.imagem.startsWith('data:') ? img.imagem : `data:image/jpeg;base64,${img.imagem}`
      }
      
      if (!imageUrl) {
        console.warn(`Image ${index} has no valid URL or base64 data:`, img)
        return null
      }
      
      return {
        id: index,
        name: img.comodo || img.nome || img.name || `Ambiente ${index + 1}`,
        url: imageUrl,
        description: img.prompt || img.descricao || img.description || '',
        room: img.comodo || img.ambiente || img.room || '',
        category: category,
        location: img.localizacao || '',
        notes: img.notas || '',
        fileSize: img.tamanho_bytes || 0
      }
    }).filter(Boolean)
    
    return NextResponse.json({
      success: true,
      data: {
        images: processedImages,
        metadata: {
          category,
          totalImages: processedImages.length,
          generatedAt: new Date().toISOString()
        }
      },
      mode: 'images'
    })

  } catch (error) {
    console.error("Error in generate-preview API:", error)
    return NextResponse.json({ 
      error: "Internal server error", 
      details: error instanceof Error ? error.message : "Unknown error"
    }, { status: 500 })
  }
}
      