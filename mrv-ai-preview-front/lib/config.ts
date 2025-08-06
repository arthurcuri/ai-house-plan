export const API_CONFIG = {
  BASE_URL: process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000",
  ENDPOINTS: {
    LOGIN: "/auth/login",
    REGISTER: "/auth/register",
  },
} as const

export const getApiUrl = (endpoint: string) => `${API_CONFIG.BASE_URL}${endpoint}`
