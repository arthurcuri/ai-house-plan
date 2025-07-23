"use client"

import { useCallback } from "react"
import { useDropzone } from "react-dropzone"
import { Upload, FileImage, File, X } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Card, CardContent } from "@/components/ui/card"

interface UploadSectionProps {
  onFileUpload: (file: File) => void
  uploadedFile: File | null
  onGeneratePreview: () => void
  isGenerating: boolean
  disabled: boolean
}

export function UploadSection({
  onFileUpload,
  uploadedFile,
  onGeneratePreview,
  isGenerating,
  disabled,
}: UploadSectionProps) {
  const onDrop = useCallback(
    (acceptedFiles: File[]) => {
      if (acceptedFiles.length > 0) {
        onFileUpload(acceptedFiles[0])
      }
    },
    [onFileUpload],
  )

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      "image/*": [".png", ".jpg", ".jpeg"],
      "application/pdf": [".pdf"],
    },
    maxFiles: 1,
    multiple: false,
  })

  const removeFile = () => {
    onFileUpload(null as any)
  }

  const getFileIcon = (file: File) => {
    if (file.type.startsWith("image/")) {
      return <FileImage className="w-6 h-6 text-emerald-600" />
    }
    return <File className="w-6 h-6 text-emerald-600" />
  }

  const formatFileSize = (bytes: number) => {
    if (bytes === 0) return "0 Bytes"
    const k = 1024
    const sizes = ["Bytes", "KB", "MB", "GB"]
    const i = Math.floor(Math.log(bytes) / Math.log(k))
    return Number.parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + " " + sizes[i]
  }

  return (
    <div className="space-y-6">
      <Card className="border-2 border-dashed border-gray-200 hover:border-emerald-300 transition-colors">
        <CardContent className="p-8">
          {!uploadedFile ? (
            <div
              {...getRootProps()}
              className={`cursor-pointer text-center space-y-4 ${isDragActive ? "bg-emerald-50" : ""}`}
            >
              <input {...getInputProps()} />
              <div className="flex justify-center">
                <div className="w-16 h-16 bg-emerald-100 rounded-full flex items-center justify-center">
                  <Upload className="w-8 h-8 text-emerald-600" />
                </div>
              </div>
              <div>
                <h3 className="text-xl font-semibold text-gray-900 mb-2">Upload Floor Plan</h3>
                <p className="text-gray-600 mb-4">
                  {isDragActive
                    ? "Drop your floor plan here..."
                    : "Drag and drop your floor plan here, or click to browse"}
                </p>
                <p className="text-sm text-gray-500">Supports PNG, JPG, JPEG, and PDF files</p>
              </div>
            </div>
          ) : (
            <div className="flex items-center justify-between p-4 bg-emerald-50 rounded-lg">
              <div className="flex items-center gap-3">
                {getFileIcon(uploadedFile)}
                <div>
                  <p className="font-medium text-gray-900">{uploadedFile.name}</p>
                  <p className="text-sm text-gray-500">{formatFileSize(uploadedFile.size)}</p>
                </div>
              </div>
              <Button variant="ghost" size="sm" onClick={removeFile} className="text-gray-500 hover:text-red-600">
                <X className="w-4 h-4" />
              </Button>
            </div>
          )}
        </CardContent>
      </Card>

      <div className="flex justify-center">
        <Button
          onClick={onGeneratePreview}
          disabled={disabled || isGenerating}
          size="lg"
          className="bg-emerald-600 hover:bg-emerald-700 text-white px-8 py-3 text-lg font-semibold min-w-[200px]"
        >
          {isGenerating ? (
            <div className="flex items-center gap-2">
              <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin" />
              Generating...
            </div>
          ) : (
            "Generate Preview"
          )}
        </Button>
      </div>
    </div>
  )
}
