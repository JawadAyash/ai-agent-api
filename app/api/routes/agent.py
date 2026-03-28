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
        logger.info({
            "event": "incoming_request",
            "session_id": payload.session_id,
            "message": payload.message
        })

        result = run_support_agent(payload.message)

        logger.info({
            "event": "agent_decision",
            "session_id": payload.session_id,
            "category": result["category"],
            "priority": result["priority"],
            "confidence": result["confidence"],
            "department": result["department"],
            "escalate": result["escalate"],
            "outage_detected": result["outage_detected"],
            "customer_id": result["customer_id"],
            "customer_found": result["customer_found"]
        })

        return AgentResponse(
            session_id=payload.session_id,
            original_message=payload.message,
            category=result["category"],
            priority=result["priority"],
            confidence=result["confidence"],
            ticket_summary=result["ticket_summary"],
            agent_response=result["response"],
            escalate=result["escalate"],
            outage_detected=result["outage_detected"],
            department=result["department"],
            customer_id=result["customer_id"],
            customer_found=result["customer_found"],
            customer_info=result["customer_info"],
            timestamp=datetime.utcnow().isoformat()
        )

    except RuntimeError as e:
        logger.error({
            "event": "error",
            "session_id": payload.session_id,
            "error": str(e)
        })
        raise HTTPException(status_code=500, detail=str(e))