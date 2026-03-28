def get_customer_info(customer_id: str):
    # Simulated database
    fake_db = {
        "123": {"name": "John Doe", "plan": "Premium", "status": "Active"},
        "456": {"name": "Jane Smith", "plan": "Basic", "status": "Inactive"},
        "789": {"name": "Alice Brown", "plan": "Enterprise", "status": "Active"},
    }

    return fake_db.get(customer_id, None)


def extract_customer_id(message: str):
    # Very simple extraction (can be improved later)
    words = message.split()

    for word in words:
        if word.isdigit():
            return word

    return None