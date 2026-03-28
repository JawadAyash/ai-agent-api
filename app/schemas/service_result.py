from pydantic import BaseModel

class OpenAIResponseResult(BaseModel):
    category: str
    priority: str
    confidence: float
    ticket_summary: str
    response: str