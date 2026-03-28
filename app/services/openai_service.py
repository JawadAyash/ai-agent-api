import json
from openai import OpenAI
from app.core.config import settings
from app.agents.prompts import SYSTEM_PROMPT
from app.schemas.service_result import OpenAIResponseResult

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def get_simple_agent_response(user_message: str) -> OpenAIResponseResult:
    try:
        response = client.responses.create(
            model=settings.OPENAI_MODEL,
            instructions=SYSTEM_PROMPT,
            input=user_message
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