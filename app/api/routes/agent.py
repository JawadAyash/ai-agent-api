from datetime import datetime
from fastapi import APIRouter, HTTPException
from app.schemas.agent import AgentRequest, AgentResponse
from app.agents.support_agent import run_support_agent

router = APIRouter(prefix="/agent", tags=["Agent"])

@router.post("/run", response_model=AgentResponse)
def run_agent(payload: AgentRequest):
    try:
        result = run_support_agent(payload.message)

        return AgentResponse(
            session_id=payload.session_id,
            category=result["category"],
            priority=result["priority"],
            agent_response=result["response"],
            timestamp=datetime.utcnow().isoformat()
        )

    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))