# Simple in-memory storage (for development only)

memory_store = {}

def get_memory(session_id: str):
    return memory_store.get(session_id, [])

def add_to_memory(session_id: str, message: str, response: str):
    if session_id not in memory_store:
        memory_store[session_id] = []

    memory_store[session_id].append({
        "message": message,
        "response": response
    })

def clear_memory(session_id: str):
    if session_id in memory_store:
        del memory_store[session_id]