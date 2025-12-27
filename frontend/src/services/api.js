import axios from 'axios'

// Determine API base URL based on environment
const getApiBaseUrl = () => {
  // In development, use proxy (handled by Vite)
  // In production, use relative URLs (same origin)
  if (import.meta.env.DEV) {
    return '/api'
  }
  return '/api'
}

const api = axios.create({
  baseURL: getApiBaseUrl(),
  headers: {
    'Content-Type': 'application/json',
  },
})

// Health check
export const healthCheck = () => api.get('/health/')

// Items API
export const fetchItems = () => api.get('/items/')
export const createItem = (data) => api.post('/items/', data)
export const updateItem = (id, data) => api.put(`/items/${id}/`, data)
export const deleteItem = (id) => api.delete(`/items/${id}/`)

export default api

