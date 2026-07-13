# AI-First CRM HCP Module – Log Interaction Screen

An advanced Customer Relationship Management (CRM) system designed for healthcare professionals (HCPs), featuring AI-powered interaction logging through LangGraph agents.

## 🎯 Project Overview

This project implements an AI-first CRM system specifically tailored for field representatives in the life sciences industry. The core feature is the **Log Interaction Screen**, which allows users to log HCP interactions via either:

1. **Structured Form Interface** - Traditional form-based data entry
2. **Conversational Chat Interface** - Natural language interaction logging powered by AI

## 🏗️ Tech Stack

### Frontend
- **Framework**: React 18
- **State Management**: Redux Toolkit
- **UI Library**: Material-UI (MUI)
- **Styling**: Tailwind CSS
- **Font**: Google Inter
- **Build Tool**: Vite

### Backend
- **Framework**: Python FastAPI
- **Database**: PostgreSQL/MySQL
- **ORM**: SQLAlchemy
- **API Documentation**: Swagger/OpenAPI

### AI & LLM
- **Agent Framework**: LangGraph
- **LLM Provider**: Groq (gemma2-9b-it model)
- **Fallback LLM**: llama-3.3-70b-versatile
- **LLM Libraries**: LangChain, Pydantic

## 📋 Core Features

### Log Interaction Screen
- **Dual Interface**: Toggle between form and chat modes
- **AI Summarization**: LLM-powered interaction summary generation
- **Entity Extraction**: Automatic extraction of key entities (HCP name, date, topics discussed)
- **Data Validation**: Client and server-side validation
- **Real-time Feedback**: Instant validation and suggestions

### LangGraph AI Agent Tools (5+ Required)

#### Core Tools (Required)
1. **Log Interaction Tool**
   - Captures interaction data from both form and chat interfaces
   - Performs LLM-based summarization and entity extraction
   - Validates and normalizes data
   - Returns structured interaction record

2. **Edit Interaction Tool**
   - Allows modification of previously logged interactions
   - Supports partial updates
   - Maintains audit trail of changes
   - Validates changes before persistence

#### Additional Sales Tools (3+)
3. **HCP Profile Lookup Tool**
   - Retrieves HCP details from database
   - Provides interaction history context
   - Returns relevant engagement metrics

4. **Call Planning Tool**
   - Generates talking points based on HCP profile and history
   - Suggests optimal call timing
   - Identifies key discussion topics

5. **Sales Forecast Tool**
   - Analyzes interaction patterns
   - Predicts engagement opportunities
   - Recommends next actions

6. **Report Generation Tool**
   - Creates interaction summaries
   - Generates weekly/monthly reports
   - Exports data in multiple formats

## 📂 Project Structure

```
aivoa/
├── frontend/                          # React application
│   ├── src/
│   │   ├── components/
│   │   │   ├── LogInteractionScreen/
│   │   │   │   ├── FormInterface.jsx
│   │   │   │   ├── ChatInterface.jsx
│   │   │   │   └── LogInteractionScreen.jsx
│   │   │   ├── Header.jsx
│   │   │   └── Sidebar.jsx
│   │   ├── pages/
│   │   │   ├── Dashboard.jsx
│   │   │   └── InteractionHistory.jsx
│   │   ├── redux/
│   │   │   ├── store.js
│   │   │   ├── interactionSlice.js
│   │   │   └── uiSlice.js
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
├── backend/                           # FastAPI application
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── models/
│   │   │   ├── interaction.py
│   │   │   └── hcp.py
│   │   ├── schemas/
│   │   │   ├── interaction.py
│   │   │   └── hcp.py
│   │   ├── routers/
│   │   │   ├── interactions.py
│   │   │   ├── hcps.py
│   │   │   └── agent.py
│   │   ├── agents/
│   │   │   ├── langgraph_agent.py
│   │   │   ├── tools/
│   │   │   │   ├── log_interaction.py
│   │   │   │   ├── edit_interaction.py
│   │   │   │   ├── hcp_profile_lookup.py
│   │   │   │   ├── call_planning.py
│   │   │   │   ├── sales_forecast.py
│   │   │   │   └── report_generation.py
│   │   │   └── prompts.py
│   │   └── crud/
│   │       ├── interaction.py
│   │       └── hcp.py
│   ├── requirements.txt
│   ├── .env.example
│   └── docker-compose.yml
└── docker-compose.yml                 # Main docker-compose for full stack
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Node.js 16+
- PostgreSQL or MySQL
- Docker & Docker Compose (optional)
- Groq API Key

### Installation

#### 1. Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Update .env with your database and Groq API credentials

# Initialize database
alembic upgrade head

# Run FastAPI server
uvicorn app.main:app --reload --port 8000
```

#### 2. Frontend Setup

```bash
cd frontend
npm install

# Create .env file
cp .env.example .env
# Update .env with API endpoint (http://localhost:8000)

# Run development server
npm run dev
```

### Using Docker Compose

```bash
# From root directory
docker-compose up -d

# Frontend: http://localhost:3000
# Backend: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

## 🔧 Configuration

### Environment Variables

**Backend (.env)**
```
DATABASE_URL=postgresql://user:password@localhost:5432/aivoa
GROQ_API_KEY=your_groq_api_key
FASTAPI_ENV=development
CORS_ORIGINS=["http://localhost:3000", "http://localhost:5173"]
```

**Frontend (.env)**
```
VITE_API_BASE_URL=http://localhost:8000
VITE_API_TIMEOUT=30000
```

## 📊 LangGraph Agent Architecture

The LangGraph agent orchestrates multiple tools to handle HCP interactions:

```
User Input → Chat Interface → LangGraph Agent
                               ↓
                    [Tool Selection & Execution]
                    ├── Log Interaction Tool
                    ├── Edit Interaction Tool
                    ├── HCP Profile Lookup
                    ├── Call Planning Tool
                    ├── Sales Forecast Tool
                    └── Report Generation Tool
                               ↓
                    Database & LLM Processing
                               ↓
                    Response to User → Chat Display
```

## 🎮 Usage

### Logging an Interaction

1. Navigate to "Log Interaction" screen
2. Choose interface:
   - **Form Mode**: Fill structured fields (HCP name, date, topics, etc.)
   - **Chat Mode**: Describe interaction naturally in conversational format
3. Click "Submit" or send message
4. AI agent processes and logs the interaction
5. View confirmation with extracted entities

### Editing an Interaction

1. Navigate to "Interaction History"
2. Select interaction to edit
3. Modify details in the provided interface
4. Save changes (audit trail maintained)

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest tests/ -v
```

### Frontend Tests
```bash
cd frontend
npm run test
```

## 📚 API Documentation

Once the backend is running, access the interactive API documentation at:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔐 Security

- Input validation on all endpoints
- CORS protection
- Environment variable-based configuration
- SQL injection prevention via ORM
- Rate limiting on API endpoints

## 📝 Database Schema

### Interactions Table
```sql
CREATE TABLE interactions (
    id UUID PRIMARY KEY,
    hcp_id UUID NOT NULL,
    interaction_date TIMESTAMP NOT NULL,
    interaction_type VARCHAR(50),
    summary TEXT,
    entities JSONB,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

### HCP Profiles Table
```sql
CREATE TABLE hcp_profiles (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    specialty VARCHAR(100),
    contact_info JSONB,
    last_interaction TIMESTAMP,
    interaction_count INT DEFAULT 0
);
```

## 🎯 Key Features Implementation

### 1. AI-Powered Summarization
- Uses Groq's LLM to generate concise summaries
- Extracts key entities and discussion points
- Maintains conversation context

### 2. Dual Interface
- Form-based: Structured data entry with validation
- Chat-based: Natural language processing with AI understanding
- Real-time switching between modes

### 3. Entity Extraction
- Automatic identification of HCP details
- Topic and product mentions
- Call outcomes and next steps

### 4. State Management
- Redux Toolkit for predictable state updates
- Real-time UI synchronization
- Undo/redo capabilities

## 🐛 Troubleshooting

### Database Connection Issues
```bash
# Verify database is running
psql postgresql://user:password@localhost:5432/aivoa -c "SELECT 1"
```

### Groq API Key Issues
```bash
# Verify API key is valid
curl https://api.groq.com/openai/v1/models -H "Authorization: Bearer YOUR_KEY"
```

### CORS Errors
- Check frontend/backend origin configuration
- Ensure both running on correct ports
- Review .env CORS_ORIGINS setting

## 📖 Additional Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [Groq API Reference](https://console.groq.com/docs/models)

## 📄 License

MIT License - See LICENSE file for details

## 👥 Contributors

- **Author**: bdhansaibunny-stack
- **Project**: AI-First CRM HCP Module Round 1 Assignment

## 📞 Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

---

**Assignment Deadline**: 36 hours from start
**Status**: In Development ✅
