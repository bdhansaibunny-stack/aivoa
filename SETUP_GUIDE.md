# AI-First CRM HCP Module - Installation & Setup Guide

## 🚀 Quick Start with Docker

### Prerequisites
- Docker & Docker Compose installed
- Groq API Key (get from https://console.groq.com/keys)

### Setup Steps

1. **Clone and Navigate**
```bash
cd aivoa
```

2. **Create Environment File**
```bash
cp .env.example .env
# Edit .env and add your Groq API key
```

3. **Start Services**
```bash
docker-compose up -d
```

4. **Verify Services**
```bash
# Check if all containers are running
docker-compose ps

# Check logs
docker-compose logs -f backend
```

5. **Access Applications**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Database: localhost:5432

## 📦 Manual Setup (Without Docker)

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Update .env with your settings
# DATABASE_URL=postgresql://user:password@localhost:5432/aivoa
# GROQ_API_KEY=your_key_here

# Create database tables
python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"

# Run server
uvicorn app.main:app --reload --port 8000
```

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Create .env file
cp .env.example .env

# Update if needed
# VITE_API_BASE_URL=http://localhost:8000

# Run development server
npm run dev
```

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

## 🛠️ Configuration

### Backend Configuration (.env)
```
DATABASE_URL=postgresql://user:password@localhost:5432/aivoa
GROQ_API_KEY=your_groq_api_key
LLM_MODEL=gemma2-9b-it
LLM_TEMPERATURE=0.7
LLM_MAX_TOKENS=1000
FASTAPI_ENV=development
DEBUG=true
CORS_ORIGINS=["http://localhost:3000","http://localhost:5173"]
```

### Frontend Configuration (.env)
```
VITE_API_BASE_URL=http://localhost:8000
VITE_API_TIMEOUT=30000
```

## 📚 API Documentation

Once backend is running:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Key Endpoints

#### Interactions
- `POST /api/v1/interactions` - Create interaction
- `GET /api/v1/interactions` - List interactions
- `GET /api/v1/interactions/{id}` - Get interaction
- `PUT /api/v1/interactions/{id}` - Update interaction
- `DELETE /api/v1/interactions/{id}` - Delete interaction

#### HCP Profiles
- `POST /api/v1/hcps` - Create HCP profile
- `GET /api/v1/hcps` - List HCP profiles
- `GET /api/v1/hcps/{id}` - Get HCP profile
- `PUT /api/v1/hcps/{id}` - Update HCP profile
- `DELETE /api/v1/hcps/{id}` - Delete HCP profile

#### AI Agent
- `POST /api/v1/agent/chat` - Send message to agent
- `GET /api/v1/agent/tools` - List available tools

## 🤖 LangGraph Agent Tools

### 1. Log Interaction
Captures and structures HCP interaction data.
```bash
Curl example:
curl -X POST http://localhost:8000/api/v1/agent/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Log an interaction with Dr. Smith. We discussed new treatment options.",
    "context": {}
  }'
```

### 2. Edit Interaction
Modifies existing interaction records.

### 3. HCP Profile Lookup
Retrieves HCP information and history.

### 4. Call Planning
Generates calling strategy and talking points.

### 5. Sales Forecast
Analyzes patterns and predicts opportunities.

### 6. Report Generation
Creates comprehensive reports and summaries.

## 🔧 Troubleshooting

### Database Connection Issues
```bash
# Verify PostgreSQL is running
psql -U aivoa_user -d aivoa -h localhost

# Check Docker container
docker-compose logs postgres
```

### API Not Responding
```bash
# Check backend logs
docker-compose logs backend

# Verify API is accessible
curl http://localhost:8000/health
```

### Frontend Can't Connect to API
- Check VITE_API_BASE_URL in frontend .env
- Verify backend is running
- Check browser console for CORS errors

### Groq API Issues
```bash
# Verify API key is valid
curl -H "Authorization: Bearer YOUR_KEY" \
  https://api.groq.com/openai/v1/models
```

## 📋 Project Structure

```
aivoa/
├── backend/
│   ├── app/
│   │   ├── agents/          # LangGraph agent implementation
│   │   ├── models/          # SQLAlchemy models
│   │   ├── schemas/         # Pydantic schemas
│   │   ├── routers/         # API routes
│   │   ├── crud/            # Database operations
│   │   ├── main.py          # FastAPI app
│   │   └── config.py        # Configuration
│   ├── tests/               # Test suite
│   ├── requirements.txt     # Python dependencies
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── redux/           # Redux store
│   │   ├── services/        # API services
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## 🚢 Deployment

### Production Deployment

1. **Build Images**
```bash
docker-compose build
```

2. **Environment Setup**
```bash
cp .env.example .env
# Update .env with production values
```

3. **Start Services**
```bash
docker-compose up -d
```

### Environment Variables for Production
```
FASTAPI_ENV=production
DEBUG=false
DATABASE_URL=postgresql://prod_user:strong_password@prod_host:5432/aivoa_prod
GROQ_API_KEY=your_production_key
CORS_ORIGINS=["https://yourdomain.com"]
```

## 📞 Support & Issues

For issues or questions:
1. Check the troubleshooting section
2. Review API documentation at /docs endpoint
3. Check container logs: `docker-compose logs -f service_name`
4. Open an issue on GitHub

## 📄 License

MIT License - See LICENSE file

## ✅ Development Checklist

- [x] Backend FastAPI setup
- [x] LangGraph agent with 6 tools
- [x] Database models (Interactions, HCPs)
- [x] Frontend React components
- [x] Redux state management
- [x] Chat and Form interfaces
- [x] API integration
- [x] Docker setup
- [x] Testing framework
- [x] Documentation

## 🎯 Next Steps

1. Add Groq API key to .env
2. Start Docker containers
3. Access frontend at http://localhost:3000
4. Test Log Interaction screen
5. Try both Form and Chat modes
6. Submit to assignment form

---

**Status**: ✅ Ready for submission
**Deadline**: 36 hours
**Submission**: https://forms.gle/XdvLNBJkbdVDGADM8
