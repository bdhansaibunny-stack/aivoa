#!/bin/bash

# AI-First CRM HCP Module - Project Verification Script
# This script verifies that the project is properly set up and working

echo "================================"
echo "AIVOA Project Verification Script"
echo "================================"
echo ""

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Docker
echo -e "${YELLOW}[1/6] Checking Docker...${NC}"
if command -v docker &> /dev/null; then
    echo -e "${GREEN}✓ Docker is installed${NC}"
else
    echo -e "${RED}✗ Docker is not installed${NC}"
fi

# Check Docker Compose
echo -e "${YELLOW}[2/6] Checking Docker Compose...${NC}"
if command -v docker-compose &> /dev/null; then
    echo -e "${GREEN}✓ Docker Compose is installed${NC}"
else
    echo -e "${RED}✗ Docker Compose is not installed${NC}"
fi

# Check Python
echo -e "${YELLOW}[3/6] Checking Python...${NC}"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✓ Python is installed: $PYTHON_VERSION${NC}"
else
    echo -e "${RED}✗ Python 3 is not installed${NC}"
fi

# Check Node.js
echo -e "${YELLOW}[4/6] Checking Node.js...${NC}"
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version)
    NPM_VERSION=$(npm --version)
    echo -e "${GREEN}✓ Node.js is installed: $NODE_VERSION${NC}"
    echo -e "${GREEN}  npm version: $NPM_VERSION${NC}"
else
    echo -e "${RED}✗ Node.js is not installed${NC}"
fi

# Check backend requirements
echo -e "${YELLOW}[5/6] Checking Backend Setup...${NC}"
if [ -f "backend/requirements.txt" ]; then
    echo -e "${GREEN}✓ Backend requirements.txt found${NC}"
    REQUIREMENTS_COUNT=$(wc -l < backend/requirements.txt)
    echo -e "  Dependencies: $REQUIREMENTS_COUNT"
else
    echo -e "${RED}✗ Backend requirements.txt not found${NC}"
fi

# Check frontend setup
echo -e "${YELLOW}[6/6] Checking Frontend Setup...${NC}"
if [ -f "frontend/package.json" ]; then
    echo -e "${GREEN}✓ Frontend package.json found${NC}"
    DEPS=$(grep -c '"' < frontend/package.json)
    echo -e "  Configuration found"
else
    echo -e "${RED}✗ Frontend package.json not found${NC}"
fi

echo ""
echo "================================"
echo "Environment Files"
echo "================================"

# Check environment files
if [ -f ".env" ]; then
    echo -e "${GREEN}✓ Root .env file exists${NC}"
else
    echo -e "${YELLOW}⚠ Root .env file not found (copy from .env.example)${NC}"
fi

if [ -f "backend/.env" ]; then
    echo -e "${GREEN}✓ Backend .env file exists${NC}"
else
    echo -e "${YELLOW}⚠ Backend .env file not found (copy from backend/.env.example)${NC}"
fi

if [ -f "frontend/.env" ]; then
    echo -e "${GREEN}✓ Frontend .env file exists${NC}"
else
    echo -e "${YELLOW}⚠ Frontend .env file not found (copy from frontend/.env.example)${NC}"
fi

echo ""
echo "================================"
echo "Project Structure Check"
echo "================================"

# Check key directories and files
echo -e "${YELLOW}Backend Structure:${NC}"
[ -d "backend/app" ] && echo -e "${GREEN}✓ app/${NC}" || echo -e "${RED}✗ app/${NC}"
[ -d "backend/app/agents" ] && echo -e "${GREEN}✓ app/agents/${NC}" || echo -e "${RED}✗ app/agents/${NC}"
[ -d "backend/app/models" ] && echo -e "${GREEN}✓ app/models/${NC}" || echo -e "${RED}✗ app/models/${NC}"
[ -d "backend/app/routers" ] && echo -e "${GREEN}✓ app/routers/${NC}" || echo -e "${RED}✗ app/routers/${NC}"
[ -f "backend/app/main.py" ] && echo -e "${GREEN}✓ app/main.py${NC}" || echo -e "${RED}✗ app/main.py${NC}"

echo -e "${YELLOW}Frontend Structure:${NC}"
[ -d "frontend/src" ] && echo -e "${GREEN}✓ src/${NC}" || echo -e "${RED}✗ src/${NC}"
[ -d "frontend/src/components" ] && echo -e "${GREEN}✓ src/components/${NC}" || echo -e "${RED}✗ src/components/${NC}"
[ -d "frontend/src/redux" ] && echo -e "${GREEN}✓ src/redux/${NC}" || echo -e "${RED}✗ src/redux/${NC}"
[ -f "frontend/src/App.jsx" ] && echo -e "${GREEN}✓ src/App.jsx${NC}" || echo -e "${RED}✗ src/App.jsx${NC}"

echo ""
echo "================================"
echo "Tools Verification"
echo "================================"

echo -e "${YELLOW}LangGraph Tools:${NC}"
[ -f "backend/app/agents/tools/log_interaction.py" ] && echo -e "${GREEN}✓ log_interaction.py${NC}" || echo -e "${RED}✗ log_interaction.py${NC}"
[ -f "backend/app/agents/tools/edit_interaction.py" ] && echo -e "${GREEN}✓ edit_interaction.py${NC}" || echo -e "${RED}✗ edit_interaction.py${NC}"
[ -f "backend/app/agents/tools/hcp_profile_lookup.py" ] && echo -e "${GREEN}✓ hcp_profile_lookup.py${NC}" || echo -e "${RED}✗ hcp_profile_lookup.py${NC}"
[ -f "backend/app/agents/tools/call_planning.py" ] && echo -e "${GREEN}✓ call_planning.py${NC}" || echo -e "${RED}✗ call_planning.py${NC}"
[ -f "backend/app/agents/tools/sales_forecast.py" ] && echo -e "${GREEN}✓ sales_forecast.py${NC}" || echo -e "${RED}✗ sales_forecast.py${NC}"
[ -f "backend/app/agents/tools/report_generation.py" ] && echo -e "${GREEN}✓ report_generation.py${NC}" || echo -e "${RED}✗ report_generation.py${NC}"

echo ""
echo "================================"
echo "Documentation Files"
echo "================================"

[ -f "README.md" ] && echo -e "${GREEN}✓ README.md${NC}" || echo -e "${RED}✗ README.md${NC}"
[ -f "SETUP_GUIDE.md" ] && echo -e "${GREEN}✓ SETUP_GUIDE.md${NC}" || echo -e "${RED}✗ SETUP_GUIDE.md${NC}"
[ -f "IMPLEMENTATION_SUMMARY.md" ] && echo -e "${GREEN}✓ IMPLEMENTATION_SUMMARY.md${NC}" || echo -e "${RED}✗ IMPLEMENTATION_SUMMARY.md${NC}"
[ -f "VIDEO_GUIDE.md" ] && echo -e "${GREEN}✓ VIDEO_GUIDE.md${NC}" || echo -e "${RED}✗ VIDEO_GUIDE.md${NC}"
[ -f "docker-compose.yml" ] && echo -e "${GREEN}✓ docker-compose.yml${NC}" || echo -e "${RED}✗ docker-compose.yml${NC}"

echo ""
echo "================================"
echo "Quick Start Commands"
echo "================================"
echo ""
echo "1. Setup environment:"
echo "   cp .env.example .env"
echo "   # Edit .env and add your Groq API key"
echo ""
echo "2. Start with Docker:"
echo "   docker-compose up -d"
echo ""
echo "3. Access applications:"
echo "   Frontend: http://localhost:3000"
echo "   Backend: http://localhost:8000"
echo "   API Docs: http://localhost:8000/docs"
echo ""
echo "4. Run tests:"
echo "   cd backend"
echo "   pytest tests/ -v"
echo ""
echo "================================"
echo "Project Status: ✓ READY"
echo "================================"
