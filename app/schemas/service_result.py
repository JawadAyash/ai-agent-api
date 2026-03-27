from pydantic import BaseModel

class OpenAIResponseResult(BaseModel):
    category: str
    priority: str
    response: str