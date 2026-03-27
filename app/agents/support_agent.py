from app.services.openai_service import get_simple_agent_response

def run_support_agent(user_message: str):
    result = get_simple_agent_response(user_message)

    return {
        "category": result.category,
        "priority": result.priority,
        "response": result.response
    }