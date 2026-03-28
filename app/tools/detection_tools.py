def detect_outage_keywords(message: str) -> bool:
    outage_keywords = [
        "system down",
        "service down",
        "outage",
        "all users",
        "production down",
        "cannot log in",
        "login not working",
        "server error",
        "500 error"
    ]

    message_lower = message.lower()

    return any(keyword in message_lower for keyword in outage_keywords)