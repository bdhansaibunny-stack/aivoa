SYSTEM_PROMPT = """You are an AI assistant for a Life Sciences CRM system.
Help users log interactions with HCPs using available tools.
"""

LOG_INTERACTION_PROMPT = "Extract and structure the following interaction information: {user_input}"
ENTITY_EXTRACTION_PROMPT = "Extract key entities from this interaction: {interaction_text}"
CALL_PLANNING_PROMPT = "Generate a call plan for HCP: {hcp_name}"
FORECAST_PROMPT = "Analyze interaction pattern for: {hcp_name}"
REPORT_PROMPT = "Generate a report for period: {period}"
