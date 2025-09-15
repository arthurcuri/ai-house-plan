import { NextRequest, NextResponse } from 'next/server'
import path from 'path'
import fs from 'fs'

export async function GET(
  request: NextRequest,
  { params }: { params: { path: string[] } }
) {
  try {
    const imagePath = params.path.join('/')
    console.log(`Requesting image path: ${imagePath}`)
    
    // Construir o caminho absoluto para a imagem
    const fullPath = path.join('/home/ak/Área de trabalho/mrv-ai/mrv-ai-preview-back/generated_images', imagePath)
    console.log(`Full path: ${fullPath}`)
    
    // Verificar se o arquivo existe
    if (!fs.existsSync(fullPath)) {
      console.error(`Image not found at: ${fullPath}`)
      return new NextResponse('Image not found', { status: 404 })
    }
    
    // Ler o arquivo
    const imageBuffer = fs.readFileSync(fullPath)
    console.log(`Successfully read image: ${imagePath}, size: ${imageBuffer.length} bytes`)
    
    // Determinar o tipo de conteúdo baseado na extensão
    const extension = path.extname(imagePath).toLowerCase()
    let contentType = 'image/jpeg'
    
    switch (extension) {
      case '.png':
        contentType = 'image/png'
        break
      case '.gif':
        contentType = 'image/gif'
        break
      case '.webp':
        contentType = 'image/webp'
        break
      case '.jpg':
      case '.jpeg':
        contentType = 'image/jpeg'
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