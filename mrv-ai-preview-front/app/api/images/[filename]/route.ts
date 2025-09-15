import { NextRequest, NextResponse } from 'next/server'

export async function GET(
  request: NextRequest,
  { params }: { params: { filename: string } }
) {
  try {
    const { filename } = params
    
    console.log(`Requesting image: ${filename}`)
    
    // Fazer proxy para o backend Python servir a imagem
    // O backend Python deve ter uma rota para servir imagens da pasta generated_images
    const imageUrl = `http://127.0.0.1:8000/images/${filename}`
    
    console.log(`Fetching from backend: ${imageUrl}`)
    
    const response = await fetch(imageUrl)
    
    if (!response.ok) {
      console.error(`Failed to fetch image from backend: ${imageUrl} - Status: ${response.status}`)
      return new NextResponse('Image not found', { status: 404 })
    }
    
    const imageBuffer = await response.arrayBuffer()
    
    console.log(`Successfully fetched image: ${filename}, size: ${imageBuffer.byteLength} bytes`)
    
    // Determinar o tipo de conteúdo baseado na extensão
    const extension = filename.split('.').pop()?.toLowerCase()
    let contentType = 'image/jpeg'
    
    switch (extension) {
      case 'png':
        contentType = 'image/png'
        break
      case 'gif':
        contentType = 'image/gif'
        break
      case 'webp':
        contentType = 'image/webp'
        break
      default:
        contentType = 'image/jpeg'
    }
    
    return new NextResponse(imageBuffer, {
      headers: {
        'Content-Type': contentType,
        'Cache-Control': 'public, max-age=3600'
      }
    })
    
  } catch (error) {
    console.error('Error serving image:', error)
    return new NextResponse('Internal server error', { status: 500 })
  }
}
