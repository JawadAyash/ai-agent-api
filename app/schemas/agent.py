from pydantic import BaseModel, Field

class AgentRequest(BaseModel):
    session_id: str = Field(..., min_length=1, max_length=100)
    message: str = Field(..., min_length=1, max_length=2000)

class AgentResponse(BaseModel):
    session_id: str
    category: str
    priority: str
    agent_response: str
    timestamp: str