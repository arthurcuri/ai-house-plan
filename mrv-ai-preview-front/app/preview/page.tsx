"use client"

import { AppInterface } from "@/components/app-interface"
import { useRouter } from "next/navigation"

export default function PreviewPage() {
  const router = useRouter()

  return <AppInterface onBackToFeatures={() => router.push("/features")} />
}

