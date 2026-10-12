from fastapi import FastAPI
from .models import EmailInput, Analysis
from .agent import analyze

app = FastAPI(title="MailMind", version="0.1.0")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "mode": "prototype"}

@app.post("/v1/analyze", response_model=Analysis)
def analyze_email(email: EmailInput) -> Analysis:
    return analyze(email)
