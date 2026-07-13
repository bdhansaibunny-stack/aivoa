import { configureStore } from '@reduxjs/toolkit'
import interactionReducer from './interactionSlice'
import uiReducer from './uiSlice'

const store = configureStore({
  reducer: {
    interactions: interactionReducer,
    ui: uiReducer
  }
})

export default store
