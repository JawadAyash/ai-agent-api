from fastapi import APIRouter
from app.services.memory_service import get_memory, clear_memory

router = APIRouter(prefix="/memory", tags=["Memory"])

@router.get("/{session_id}")
def read_memory(session_id: str):
    return {
        "session_id": session_id,
        "history": get_memory(session_id)
    }

@router.delete("/{session_id}")
def delete_memory(session_id: str):
    clear_memory(session_id)

    return {
        "session_id": session_id,
        "message": "Memory cleared successfully"
    }