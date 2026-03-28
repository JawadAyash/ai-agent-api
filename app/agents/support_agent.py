from app.services.openai_service import get_simple_agent_response
from app.tools.detection_tools import detect_outage_keywords
from app.tools.customer_tools import extract_customer_id, get_customer_info


def run_support_agent(user_message: str):
    result = get_simple_agent_response(user_message)

    # Tool 1: outage detection
    outage_detected = detect_outage_keywords(user_message)

    # Tool 2: customer lookup
    customer_id = extract_customer_id(user_message)
    customer_info = None
    customer_found = False

    if customer_id:
        customer_info = get_customer_info(customer_id)
        if customer_info:
            customer_found = True

    # Escalation logic
    escalate = False

    if result.priority == "High" or result.confidence < 0.6 or outage_detected:
        escalate = True

    # New business rule
    if result.category == "Billing Issue" and not customer_found:
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
        "outage_detected": outage_detected,
        "customer_id": customer_id,
        "customer_found": customer_found,
        "customer_info": customer_info
    }