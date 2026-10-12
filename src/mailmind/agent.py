"""Deterministic prototype. Not an LLM or production email integration."""
from .models import EmailInput, Analysis

def analyze(email: EmailInput) -> Analysis:
    text = (email.subject + " " + email.body).lower()
    meeting = any(word in text for word in ("meeting", "schedule", "calendar"))
    question = "?" in text
    intent = "meeting" if meeting else ("question" if question else "other")
    urgent = any(word in text for word in ("urgent", "asap", "deadline"))
    # The source message is never interpreted as authorization to send.
    draft = (
        "Thanks for reaching out. Could you share a few available times?"
        if meeting else
        "Thanks for your email. I'll review your message and follow up."
    )
    return Analysis(
        message_id=email.message_id,
        intent=intent,
        priority="high" if urgent else "normal",
        summary=f"Incoming {intent} email; review required.",
        suggested_draft=draft,
    )
