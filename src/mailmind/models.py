from typing import Literal
from pydantic import BaseModel, Field

class EmailInput(BaseModel):
    message_id: str = Field(min_length=1, max_length=256)
    sender: str = Field(min_length=3, max_length=320)
    subject: str = Field(default="", max_length=998)
    body: str = Field(default="", max_length=100000)

class Analysis(BaseModel):
    message_id: str
    intent: Literal["meeting", "question", "other"]
    priority: Literal["normal", "high"]
    requires_approval: bool = True
    action: Literal["draft_only"] = "draft_only"
    summary: str
    suggested_draft: str
