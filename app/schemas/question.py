from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class QuestionResponse(BaseModel):
    user_question_id: int
    question: str


class UserQuestionResponse(BaseModel):
    id: int
    question_text: str
    created_at: datetime
    diary_id: Optional[int] = None

    class Config:
        from_attributes = True
