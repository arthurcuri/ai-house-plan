// Utilitário para trabalhar com JWT no frontend
export interface TokenPayload {
  sub: string // email
  nome: string
  user_id: number
  exp: number
  iat: number
}

export class TokenManager {
  private static TOKEN_KEY = 'house-ai-token'
  private static USER_KEY = 'house-ai-user'

  static getToken(): string | null {
    if (typeof window === 'undefined') return null
    return localStorage.getItem(this.TOKEN_KEY)
  }

  static setToken(token: string): void {
    if (typeof window === 'undefined') return
    localStorage.setItem(this.TOKEN_KEY, token)
  }

  static removeToken(): void {
    if (typeof window === 'undefined') return
    localStorage.removeItem(this.TOKEN_KEY)
    localStorage.removeItem(this.USER_KEY)
  }

  static isTokenExpired(token: string): boolean {
    try {
      const payload = this.decodeToken(token)
      if (!payload) return true
      
      const currentTime = Math.floor(Date.now() / 1000)
      return payload.exp < currentTime
    } catch {
      return true
    }
  }

  static decodeToken(token: string): TokenPayload | null {
    try {
      const base64Url = token.split('.')[1]
      const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/')
      const jsonPayload = decodeURIComponent(
        atob(base64)
          .split('')
          .map(c => '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2))
          .join('')
      )
      return JSON.parse(jsonPayload)
    } catch {
      return null
    }
  }

  static async validateTokenWithServer(): Promise<boolean> {
    const token = this.getToken()
    if (!token) return false

    try {
      const response = await fetch('/api/validate-token', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      })
      return response.ok
    } catch {
      return false
    }
  }

  static getAuthHeaders(): HeadersInit {
    const token = this.getToken()
    return token ? { 'Authorization': `Bearer ${token}` } : {}
  }
}
