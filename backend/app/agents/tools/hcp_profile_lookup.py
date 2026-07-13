from typing import Dict, Any
from datetime import datetime

def hcp_profile_lookup(hcp_name: str, include_history: bool = True) -> Dict[str, Any]:
    """Look up HCP profile"""
    try:
        profile = {
            "hcp_name": hcp_name,
            "specialty": "Not specified",
            "total_interactions": 0,
            "engagement_level": "New"
        }
        return {"success": True, "message": f"Profile found", "profile": profile}
    except Exception as e:
        return {"success": False, "error": str(e)}
