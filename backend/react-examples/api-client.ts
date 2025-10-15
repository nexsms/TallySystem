// API Client for React Frontend
// Base configuration for making API calls to FastAPI backend

const API_BASE_URL = process.env.REACT_APP_API_URL || "http://localhost:8000"

// Helper function to get auth token from localStorage
const getAuthToken = (): string | null => {
  return localStorage.getItem("access_token")
}

// Helper function to make authenticated requests
export const apiClient = async (endpoint: string, options: RequestInit = {}): Promise<any> => {
  const token = getAuthToken()

  const headers: HeadersInit = {
    "Content-Type": "application/json",
    ...options.headers,
  }

  if (token) {
    headers["Authorization"] = `Bearer ${token}`
  }

  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    ...options,
    headers,
  })

  if (!response.ok) {
    const error = await response.json()
    throw new Error(error.detail || "API request failed")
  }

  return response.json()
}

// Authentication API calls
export const authAPI = {
  login: async (username: string, password: string) => {
    const formData = new URLSearchParams()
    formData.append("username", username)
    formData.append("password", password)

    const response = await fetch(`${API_BASE_URL}/api/auth/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: formData,
    })

    if (!response.ok) {
      throw new Error("Login failed")
    }

    const data = await response.json()
    localStorage.setItem("access_token", data.access_token)
    return data
  },

  register: async (userData: {
    username: string
    email: string
    password: string
    full_name: string
    role?: string
  }) => {
    return apiClient("/api/auth/register", {
      method: "POST",
      body: JSON.stringify(userData),
    })
  },

  logout: () => {
    localStorage.removeItem("access_token")
  },

  getCurrentUser: async () => {
    return apiClient("/api/auth/me")
  },
}

// Tally API calls
export const tallyAPI = {
  getAll: async (skip = 0, limit = 100) => {
    return apiClient(`/api/tallies/?skip=${skip}&limit=${limit}`)
  },

  getById: async (id: number) => {
    return apiClient(`/api/tallies/${id}`)
  },

  create: async (tallyData: {
    location: string
    constituency: string
    ward: string
    polling_station: string
    registered_voters: number
    votes_cast: number
    candidate_votes: number
  }) => {
    return apiClient("/api/tallies/", {
      method: "POST",
      body: JSON.stringify(tallyData),
    })
  },

  update: async (id: number, tallyData: any) => {
    return apiClient(`/api/tallies/${id}`, {
      method: "PUT",
      body: JSON.stringify(tallyData),
    })
  },

  delete: async (id: number) => {
    return apiClient(`/api/tallies/${id}`, {
      method: "DELETE",
    })
  },
}

// Dashboard API calls
export const dashboardAPI = {
  getStats: async () => {
    return apiClient("/api/dashboard/stats")
  },

  getByConstituency: async () => {
    return apiClient("/api/dashboard/by-constituency")
  },

  getByWard: async () => {
    return apiClient("/api/dashboard/by-ward")
  },
}

// User API calls
export const userAPI = {
  getAll: async (skip = 0, limit = 100) => {
    return apiClient(`/api/users/?skip=${skip}&limit=${limit}`)
  },

  getById: async (id: number) => {
    return apiClient(`/api/users/${id}`)
  },

  update: async (id: number, userData: any) => {
    return apiClient(`/api/users/${id}`, {
      method: "PUT",
      body: JSON.stringify(userData),
    })
  },

  delete: async (id: number) => {
    return apiClient(`/api/users/${id}`, {
      method: "DELETE",
    })
  },
}
