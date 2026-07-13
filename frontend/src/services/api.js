import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'
const API_TIMEOUT = import.meta.env.VITE_API_TIMEOUT || 30000

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: API_TIMEOUT
})

export const interactionAPI = {
  create: (data) => api.post('/api/v1/interactions', data),
  get: (id) => api.get(`/api/v1/interactions/${id}`),
  list: (skip = 0, limit = 100) => api.get('/api/v1/interactions', { params: { skip, limit } }),
  update: (id, data) => api.put(`/api/v1/interactions/${id}`, data),
  delete: (id) => api.delete(`/api/v1/interactions/${id}`)
}

export const hcpAPI = {
  create: (data) => api.post('/api/v1/hcps', data),
  get: (id) => api.get(`/api/v1/hcps/${id}`),
  list: (skip = 0, limit = 100) => api.get('/api/v1/hcps', { params: { skip, limit } }),
  update: (id, data) => api.put(`/api/v1/hcps/${id}`, data),
  delete: (id) => api.delete(`/api/v1/hcps/${id}`)
}

export const agentAPI = {
  chat: (message, context = {}) => api.post('/api/v1/agent/chat', { message, context }),
  getTools: () => api.get('/api/v1/agent/tools')
}

export default api
