import json
from openai import OpenAI
from app.core.config import settings
from app.agents.prompts import SYSTEM_PROMPT
from app.schemas.service_result import OpenAIResponseResult
from app.services.memory_service import get_memory

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def get_simple_agent_response(user_message: str, session_id: str) -> OpenAIResponseResult:
    try:
        history = get_memory(session_id)

        # Build conversation context
        conversation = ""

        for item in history:
            conversation += f"User: {item['message']}\n"
            conversation += f"Agent: {item['response']}\n"

        full_input = f"""
Conversation history:
{conversation}

Current user message:
{user_message}
"""

        response = client.responses.create(
            model=settings.OPENAI_MODEL,
            instructions=SYSTEM_PROMPT,
            input=full_input
        )

        text_output = response.output_text
        parsed = json.loads(text_output)

        return OpenAIResponseResult(
            category=parsed["category"],
            priority=parsed["priority"],
            confidence=parsed["confidence"],
            ticket_summary=parsed["ticket_summary"],
            response=parsed["response"]
        )

    except Exception as e:
        raise RuntimeError(f"OpenAI request failed: {str(e)}")