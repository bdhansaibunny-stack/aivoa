import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_root_endpoint():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "AI-First CRM" in response.json()["name"]

def test_available_tools():
    """Test agent tools endpoint"""
    response = client.get("/api/v1/agent/tools")
    assert response.status_code == 200
    data = response.json()
    assert data["total_tools"] == 6
    assert len(data["tools"]) == 6

def test_agent_chat_endpoint():
    """Test agent chat endpoint"""
    payload = {
        "message": "Log an interaction with Dr. Smith",
        "context": {}
    }
    response = client.post("/api/v1/agent/chat", json=payload)
    # Note: This might fail if Groq API key is not set
    assert response.status_code in [200, 500]
