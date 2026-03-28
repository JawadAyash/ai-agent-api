from datetime import datetime
from fastapi import APIRouter, HTTPException
from app.schemas.agent import AgentRequest, AgentResponse
from app.agents.support_agent import run_support_agent
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/agent", tags=["Agent"])

@router.post("/run", response_model=AgentResponse)
def run_agent(payload: AgentRequest):
    try:
        logger.info(f"Incoming request: {payload.message}")

        result = run_support_agent(payload.message)

        logger.info(f"Category: {result['category']}, Priority: {result['priority']}, Department: {result['department']}")

        return AgentResponse(
            session_id=payload.session_id,
            original_message=payload.message,
            category=result["category"],
            priority=result["priority"],
            confidence=result["confidence"],
            ticket_summary=result["ticket_summary"],
            agent_response=result["response"],
            escalate=result["escalate"],
            department=result["department"],
            timestamp=datetime.utcnow().isoformat()
        )

    except RuntimeError as e:
        logger.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))