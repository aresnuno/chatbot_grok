from config import journeys

def generate_prompt(session):
    journey = session.get("journey")
    topic = session.get("topic")
    subtopic = session.get("subtopic")

    if journey and journey in journeys:
        if topic and topic in journeys[journey]["topics"]:
            if subtopic and subtopic in journeys[journey]["topics"][topic]["subtopics"]:
                return journeys[journey]["topics"][topic]["subtopics"][subtopic]
            return journeys[journey]["topics"][topic]["default_response"]
        return journeys[journey]["default_response"]
    return "Halo! Ada yang bisa saya bantu hari ini?"

def update_session(session, user_input):
    user_input = user_input.lower()
    if "akun" in user_input:
        session["journey"] = "fintech_support"
        session["topic"] = "account"
        session["subtopic"] = None
    elif "password" in user_input:
        session["journey"] = "fintech_support"
        session["topic"] = "account"
        session["subtopic"] = "reset_password"
    elif "email" in user_input:
        session["journey"] = "fintech_support"
        session["topic"] = "account"
        session["subtopic"] = "update_email"
    elif "bayar" in user_input or "payment" in user_input:
        session["journey"] = "fintech_support"
        session["topic"] = "payment"
        session["subtopic"] = None
    elif "gagal" in user_input:
        session["journey"] = "fintech_support"
        session["topic"] = "payment"
        session["subtopic"] = "failed_payment"
    elif "refund" in user_input:
        session["journey"] = "fintech_support"
        session["topic"] = "payment"
        session["subtopic"] = "refund"
    else:
        # Reset kalau tidak dikenali
        session["journey"] = None
        session["topic"] = None
        session["subtopic"] = None

    return session
