from typing import Dict, Any
from datetime import datetime

def log_interaction(hcp_name: str, interaction_date: str, interaction_type: str, 
                     summary: str, topics: str, outcomes: str, next_steps: str) -> Dict[str, Any]:
    """Log an HCP interaction"""
    try:
        interaction_data = {
            "hcp_name": hcp_name.strip(),
            "interaction_date": interaction_date,
            "interaction_type": interaction_type.lower(),
            "summary": summary.strip(),
            "topics": [t.strip() for t in topics.split(",") if t.strip()],
            "outcomes": outcomes.strip(),
            "next_steps": next_steps.strip(),
            "extracted_at": datetime.now().isoformat(),
            "status": "logged"
        }
        return {"success": True, "message": f"Interaction with {hcp_name} logged", "interaction": interaction_data}
    except Exception as e:
        return {"success": False, "error": str(e)}
