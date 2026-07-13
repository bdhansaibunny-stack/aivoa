import React from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { setMode } from '../redux/uiSlice'
import FormInterface from './LogInteractionScreen/FormInterface'
import ChatInterface from './LogInteractionScreen/ChatInterface'
import './LogInteractionScreen.css'

const LogInteractionScreen = () => {
  const dispatch = useDispatch()
  const mode = useSelector(state => state.ui.mode)

  return (
    <div className="log-interaction-container">
      <div className="mode-selector">
        <button
          className={`mode-btn ${mode === 'form' ? 'active' : ''}`}
          onClick={() => dispatch(setMode('form'))}
        >
          📋 Form
        </button>
        <button
          className={`mode-btn ${mode === 'chat' ? 'active' : ''}`}
          onClick={() => dispatch(setMode('chat'))}
        >
          💬 Chat
        </button>
      </div>

      <div className="interface-container">
        {mode === 'form' ? <FormInterface /> : <ChatInterface />}
      </div>
    </div>
  )
}

export default LogInteractionScreen
