import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Header from './components/Header'
import Sidebar from './components/Sidebar'
import LogInteractionScreen from './components/LogInteractionScreen/LogInteractionScreen'
import './App.css'

const App = () => {
  return (
    <Router>
      <div className="app">
        <Header />
        <div className="app-container">
          <Sidebar />
          <main className="main-content">
            <Routes>
              <Route path="/" element={<LogInteractionScreen />} />
              <Route path="/log-interaction" element={<LogInteractionScreen />} />
              <Route path="*" element={<LogInteractionScreen />} />
            </Routes>
          </main>
        </div>
      </div>
    </Router>
  )
}

export default App
