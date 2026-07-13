import React from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { toggleSidebar } from '../redux/uiSlice'
import './Header.css'

const Header = () => {
  const dispatch = useDispatch()
  const sidebarOpen = useSelector(state => state.ui.sidebarOpen)

  return (
    <header className="header">
      <div className="header-content">
        <button
          className="toggle-sidebar-btn"
          onClick={() => dispatch(toggleSidebar())}
          title="Toggle Sidebar"
        >
          ☰
        </button>
        <h1>🏥 AI-First CRM HCP Module</h1>
        <div className="header-actions">
          <span className="status">✓ Online</span>
        </div>
      </div>
    </header>
  )
}

export default Header
