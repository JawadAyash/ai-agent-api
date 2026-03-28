from pydantic import BaseModel, Field

class AgentRequest(BaseModel):
    session_id: str = Field(..., min_length=1, max_length=100)
    message: str = Field(..., min_length=1, max_length=2000)

class AgentResponse(BaseModel):
    session_id: str
    original_message: str
    category: str
    priority: str
    confidence: float
    ticket_summary: str
    agent_response: str
    escalate: bool
    outage_detected: bool
    department: str
    timestamp: str