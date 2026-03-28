ticket_counter = 1000
created_tickets = []

def create_ticket(category: str, priority: str, summary: str, department: str):
    global ticket_counter

    ticket_counter += 1
    ticket_id = f"TICK-{ticket_counter}"

    ticket = {
        "ticket_id": ticket_id,
        "category": category,
        "priority": priority,
        "summary": summary,
        "department": department,
        "status": "Created"
    }

    created_tickets.append(ticket)

    return ticket