import pytest
import asyncio
from app.agents.langgraph_agent import agent
from app.agents.tools.log_interaction import log_interaction
from app.agents.tools.edit_interaction import edit_interaction
from app.agents.tools.hcp_profile_lookup import hcp_profile_lookup
from app.agents.tools.call_planning import call_planning
from app.agents.tools.sales_forecast import sales_forecast
from app.agents.tools.report_generation import report_generation

def test_log_interaction_tool():
    """Test log interaction tool"""
    result = log_interaction(
        hcp_name="Dr. Smith",
        interaction_date="2024-01-15",
        interaction_type="phone",
        summary="Discussed new treatment options",
        topics="Product A, Patient Outcomes",
        outcomes="Positive",
        next_steps="Schedule follow-up call"
    )
    assert result["success"] == True
    assert result["interaction"]["hcp_name"] == "Dr. Smith"

def test_edit_interaction_tool():
    """Test edit interaction tool"""
    result = edit_interaction(
        interaction_id="test-123",
        hcp_name="Dr. Johnson",
        summary="Updated summary"
    )
    assert result["success"] == True

def test_hcp_profile_lookup_tool():
    """Test HCP profile lookup tool"""
    result = hcp_profile_lookup(hcp_name="Dr. Smith")
    assert result["success"] == True
    assert result["profile"]["hcp_name"] == "Dr. Smith"

def test_call_planning_tool():
    """Test call planning tool"""
    result = call_planning(
        hcp_name="Dr. Smith",
        hcp_specialty="Cardiology"
    )
    assert result["success"] == True
    assert len(result["call_plan"]["talking_points"]) > 0

def test_sales_forecast_tool():
    """Test sales forecast tool"""
    result = sales_forecast(
        hcp_name="Dr. Smith",
        current_status="active"
    )
    assert result["success"] == True
    assert "opportunity_score" in result["forecast"]

def test_report_generation_tool():
    """Test report generation tool"""
    result = report_generation(
        report_type="summary",
        period="monthly"
    )
    assert result["success"] == True
    assert result["report"]["period"] == "monthly"

@pytest.mark.asyncio
async def test_agent_run():
    """Test agent execution"""
    result = await agent.run("Log an interaction with Dr. Smith")
    assert result["success"] == True
    assert result["timestamp"] is not None
