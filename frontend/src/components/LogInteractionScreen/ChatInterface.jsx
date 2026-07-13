import React, { useState, useRef, useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { addInteraction, setLoading } from '../../redux/interactionSlice'
import { agentAPI } from '../../services/api'
import './ChatInterface.css'

const ChatInterface = () => {
  const dispatch = useDispatch()
  const [messages, setMessages] = useState([
    { id: 1, type: 'assistant', text: 'Hello! I\'m your AI assistant. I can help you log HCP interactions. Just describe your interaction naturally, and I\'ll extract and structure the information for you.' }
  ])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const messagesEndRef = useRef(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const handleSendMessage = async () => {
    if (!input.trim()) return

    const userMessage = {
      id: messages.length + 1,
      type: 'user',
      text: input
    }

    setMessages(prev => [...prev, userMessage])
    setInput('')
    setLoading(true)

    try {
      const response = await agentAPI.chat(input)
      const assistantMessage = {
        id: messages.length + 2,
        type: 'assistant',
        text: response.data.response,
        toolsCalled: response.data.tool_calls_made
      }
      setMessages(prev => [...prev, assistantMessage])
    } catch (error) {
      const errorMessage = {
        id: messages.length + 2,
        type: 'assistant',
        text: `Error: ${error.message}. Please try again.`
      }
      setMessages(prev => [...prev, errorMessage])
    } finally {
      setLoading(false)
    }
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSendMessage()
    }
  }

  return (
    <div className="chat-interface">
      <h2>💬 Log Interaction - Chat Interface</h2>
      <div className="chat-container">
        <div className="messages">
          {messages.map(msg => (
            <div key={msg.id} className={`message ${msg.type}`}>
              <div className="message-content">
                <p>{msg.text}</p>
                {msg.toolsCalled !== undefined && (
                  <small className="tools-info">Tools used: {msg.toolsCalled}</small>
                )}
              </div>
            </div>
          ))}
          {loading && (
            <div className="message assistant">
              <div className="message-content">
                <div className="typing-indicator">
                  <span></span>
                  <span></span>
                  <span></span>
                </div>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>
      </div>
      <div className="input-area">
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Describe your HCP interaction here..."
          rows="3"
          disabled={loading}
        />
        <button
          onClick={handleSendMessage}
          disabled={loading || !input.trim()}
          className="send-btn"
        >
          {loading ? 'Processing...' : 'Send'}
        </button>
      </div>
    </div>
  )
}

export default ChatInterface
