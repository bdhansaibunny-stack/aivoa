import { createSlice } from '@reduxjs/toolkit'

const initialState = {
  interactions: [],
  currentInteraction: null,
  loading: false,
  error: null,
  hcps: [],
  currentHCP: null
}

const interactionSlice = createSlice({
  name: 'interactions',
  initialState,
  reducers: {
    setLoading: (state, action) => {
      state.loading = action.payload
    },
    setError: (state, action) => {
      state.error = action.payload
    },
    setInteractions: (state, action) => {
      state.interactions = action.payload
    },
    addInteraction: (state, action) => {
      state.interactions.push(action.payload)
    },
    updateInteraction: (state, action) => {
      const index = state.interactions.findIndex(i => i.id === action.payload.id)
      if (index !== -1) {
        state.interactions[index] = action.payload
      }
    },
    deleteInteraction: (state, action) => {
      state.interactions = state.interactions.filter(i => i.id !== action.payload)
    },
    setCurrentInteraction: (state, action) => {
      state.currentInteraction = action.payload
    },
    setHCPs: (state, action) => {
      state.hcps = action.payload
    },
    setCurrentHCP: (state, action) => {
      state.currentHCP = action.payload
    }
  }
})

export const {
  setLoading,
  setError,
  setInteractions,
  addInteraction,
  updateInteraction,
  deleteInteraction,
  setCurrentInteraction,
  setHCPs,
  setCurrentHCP
} = interactionSlice.actions

export default interactionSlice.reducer
