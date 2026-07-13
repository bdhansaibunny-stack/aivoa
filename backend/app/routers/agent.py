from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from app.agents.langgraph_agent import agent

router = APIRouter(prefix="/api/v1/agent", tags=["agent"])

class AgentRequest(BaseModel):
    message: str
    context: Dict[str, Any] = {}

class AgentResponse(BaseModel):
    success: bool
    response: str
    tool_calls_made: int
    timestamp: str

@router.post("/chat", response_model=AgentResponse)
async def agent_chat(request: AgentRequest):
    try:
        result = await agent.run(request.message)
        return AgentResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent execution failed: {str(e)}")

@router.get("/tools")
def get_available_tools():
    tools_info = [{"name": tool["name"]} for tool in agent.tools]
    return {"total_tools": len(tools_info), "tools": tools_info}
