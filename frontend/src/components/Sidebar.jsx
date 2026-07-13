import React from 'react'
import { useSelector } from 'react-redux'
import './Sidebar.css'

const Sidebar = () => {
  const sidebarOpen = useSelector(state => state.ui.sidebarOpen)

  return (
    <aside className={`sidebar ${sidebarOpen ? 'open' : 'closed'}`}>
      <nav className="sidebar-nav">
        <div className="nav-section">
          <h3>Main</h3>
          <ul>
            <li><a href="/">📊 Dashboard</a></li>
            <li><a href="/log-interaction">📝 Log Interaction</a></li>
            <li><a href="/history">📋 Interaction History</a></li>
          </ul>
        </div>
        <div className="nav-section">
          <h3>Management</h3>
          <ul>
            <li><a href="/hcps">👥 HCP Profiles</a></li>
            <li><a href="/reports">📈 Reports</a></li>
            <li><a href="/settings">⚙️ Settings</a></li>
          </ul>
        </div>
        <div className="nav-section">
          <h3>Tools</h3>
          <ul>
            <li><a href="/agent">🤖 AI Agent</a></li>
            <li><a href="/api-docs">📚 API Docs</a></li>
          </ul>
        </div>
      </nav>
    </aside>
  )
}

export default Sidebar
