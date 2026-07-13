#!/bin/bash

# Stop and clean up all services

echo "🛑 Stopping AI-First CRM HCP Module services..."
echo ""

docker-compose down

echo "✅ All services stopped."
echo ""
echo "💾 Data persisted in PostgreSQL volume (postgres_data)"
echo ""
echo "To also remove data volumes, run:"
echo "   docker-compose down -v"
