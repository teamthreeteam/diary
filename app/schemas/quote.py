from pydantic import BaseModel
from typing import Optional

# 명언의 기본 구조
class QuoteBase(BaseModel):
    author: str
    content: str
    category: str

# 생성할 때 사용하는 스키마
class QuoteCreate(QuoteBase):
    pass

# API 응답으로 내보낼 때 사용하는 스키마
class QuoteResponse(QuoteBase):
    id: int

    class Config:
        # Tortoise ORM 모델 객체를 Pydantic으로 자동 변환해주는 설정입니다.
        from_attributes = True