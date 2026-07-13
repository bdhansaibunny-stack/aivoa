from typing import Dict, Any
from datetime import datetime

def edit_interaction(interaction_id: str, hcp_name: str = None, summary: str = None) -> Dict[str, Any]:
    """Edit an existing interaction"""
    try:
        updates = {}
        if hcp_name:
            updates["hcp_name"] = hcp_name
        if summary:
            updates["summary"] = summary
        updates["updated_at"] = datetime.now().isoformat()
        return {"success": True, "message": f"Interaction {interaction_id} updated", "updates": updates}
    except Exception as e:
        return {"success": False, "error": str(e)}
