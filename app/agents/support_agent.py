from app.services.openai_service import get_simple_agent_response
from app.tools.detection_tools import detect_outage_keywords

def run_support_agent(user_message: str):
    result = get_simple_agent_response(user_message)

    # Tool-based detection
    outage_detected = detect_outage_keywords(user_message)

    # Escalation logic
    escalate = False
    if result.priority == "High" or result.confidence < 0.6 or outage_detected:
        escalate = True

    # Routing logic
    routing_map = {
        "Bug Report": "Engineering",
        "Technical Question": "IT Support",
        "Billing Issue": "Finance",
        "Feature Request": "Product",
        "General Inquiry": "Customer Support"
    }

    department = routing_map.get(result.category, "Customer Support")

    return {
        "category": result.category,
        "priority": result.priority,
        "confidence": result.confidence,
        "ticket_summary": result.ticket_summary,
        "response": result.response,
        "escalate": escalate,
        "department": department,
        "outage_detected": outage_detected
    }