from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DiaryCreate(BaseModel):
    title: str
    content: str
    date: datetime

class DiaryUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    date: Optional[datetime] = None

class Diary(DiaryCreate):
    id: int
    user_id: int 
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True