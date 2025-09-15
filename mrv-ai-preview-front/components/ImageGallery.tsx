"use client"

import React, { useState } from 'react'
import Image from 'next/image'

interface GeneratedImage {
  id: number
  name: string
  url: string
  description: string
  room: string
  category: string
}

interface ImageGalleryProps {
  images: GeneratedImage[]
  category: string
  onClose?: () => void
  isLoading?: boolean
}

export default function ImageGallery({ images, category, onClose, isLoading }: ImageGalleryProps) {
  const [selectedImage, setSelectedImage] = useState<GeneratedImage | null>(null)

  if (isLoading) {
    return (
      <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
        <div className="bg-white rounded-lg p-8 text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <div className="text-lg font-medium mb-2">Gerando imagens...</div>
          <div className="text-sm text-gray-600">Isso pode levar alguns minutos</div>
        </div>
      </div>
    )
  }

  if (!images || images.length === 0) {
    return (
      <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
        <div className="bg-white rounded-lg p-8 text-center">
          <div className="text-lg font-medium mb-2">Nenhuma imagem gerada</div>
          <div className="text-sm text-gray-600 mb-4">Tente novamente com uma planta diferente</div>
          {onClose && (
            <button
              onClick={onClose}
              className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
            >
              Fechar
            </button>
          )}
        </div>
      </div>
    )
  }

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-lg max-w-6xl max-h-[90vh] overflow-hidden w-full">
        {/* Header */}
        <div className="bg-blue-600 text-white p-4 flex justify-between items-center">
          <div>
            <h2 className="text-xl font-bold">
              Catálogo de Imagens - {category.toUpperCase()}
            </h2>
            <p className="text-blue-100 text-sm">
              {images.length} {images.length === 1 ? 'imagem gerada' : 'imagens geradas'}
            </p>
          </div>
          {onClose && (
            <button
              onClick={onClose}
              className="text-white hover:text-gray-200 text-2xl font-bold w-8 h-8 flex items-center justify-center"
            >
              ×
            </button>
          )}
        </div>

        {/* Grid de imagens */}
        <div className="p-6 overflow-y-auto max-h-[calc(90vh-80px)]">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {images.map((image) => (
              <div 
                key={image.id} 
                className="bg-white rounded-lg shadow-lg overflow-hidden cursor-pointer transform hover:scale-105 transition-transform duration-200 border"
                onClick={() => setSelectedImage(image)}
              >
                <div className="relative h-48">
                  <Image
                    src={image.url}
                    alt={image.name}
                    fill
                    className="object-cover"
                    sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
                  />
                </div>
                <div className="p-4">
                  <h3 className="font-semibold text-lg text-gray-800 mb-2 line-clamp-1">
                    {image.name}
                  </h3>
                  {image.room && (
                    <p className="text-sm text-blue-600 mb-2">
                      📍 {image.room}
                    </p>
                  )}
                  {image.description && (
                    <p className="text-sm text-gray-600 line-clamp-2">
                      {image.description}
                    </p>
                  )}
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Modal para imagem ampliada */}
      {selectedImage && (
        <div 
          className="fixed inset-0 bg-black bg-opacity-90 flex items-center justify-center z-[60] p-4"
          onClick={() => setSelectedImage(null)}
        >
          <div className="max-w-5xl max-h-full bg-white rounded-lg overflow-hidden">
            <div className="relative">
              <Image
                src={selectedImage.url}
                alt={selectedImage.name}
                width={1000}
                height={700}
                className="object-contain max-h-[80vh]"
              />
              <button
                onClick={(e) => {
                  e.stopPropagation()
                  setSelectedImage(null)
                }}
                className="absolute top-4 right-4 bg-white bg-opacity-80 hover:bg-opacity-100 rounded-full p-2 text-gray-800 text-xl font-bold w-8 h-8 flex items-center justify-center"
              >
                ×
              </button>
            </div>
            <div className="p-6">
              <h3 className="text-xl font-bold text-gray-800 mb-2">
                {selectedImage.name}
              </h3>
              {selectedImage.room && (
                <p className="text-blue-600 mb-2 font-medium">📍 {selectedImage.room}</p>
              )}
              {selectedImage.description && (
                <p className="text-gray-600">{selectedImage.description}</p>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
