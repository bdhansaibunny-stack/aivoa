import { createSlice } from '@reduxjs/toolkit'

const initialState = {
  mode: 'form', // 'form' or 'chat'
  theme: 'light',
  sidebarOpen: true
}

const uiSlice = createSlice({
  name: 'ui',
  initialState,
  reducers: {
    setMode: (state, action) => {
      state.mode = action.payload
    },
    setTheme: (state, action) => {
      state.theme = action.payload
    },
    toggleSidebar: (state) => {
      state.sidebarOpen = !state.sidebarOpen
    }
  }
})

export const { setMode, setTheme, toggleSidebar } = uiSlice.actions
export default uiSlice.reducer
