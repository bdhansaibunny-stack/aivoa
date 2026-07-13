#!/bin/bash

# Quick start script for the AI-First CRM HCP Module

echo "🚀 Starting AI-First CRM HCP Module..."
echo ""

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found. Creating from .env.example..."
    cp .env.example .env
    echo "✅ .env created. Please edit it and add your Groq API key."
    echo ""
fi

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker and try again."
    exit 1
fi

echo "🐳 Starting Docker containers..."
echo ""

# Start services
docker-compose up -d

# Wait for services to be ready
echo "⏳ Waiting for services to be ready..."
sleep 5

# Check if services are running
echo ""
echo "📊 Service Status:"
docker-compose ps

echo ""
echo "✅ Services started!"
echo ""
echo "📱 Access your applications:"
echo "   Frontend: http://localhost:3000"
echo "   Backend: http://localhost:8000"
echo "   API Docs: http://localhost:8000/docs"
echo ""
echo "📋 Useful commands:"
echo "   View logs: docker-compose logs -f [service]"
echo "   Stop services: docker-compose down"
echo "   Rebuild: docker-compose build"
echo ""
echo "🎉 Ready to go! Open http://localhost:3000 in your browser."
