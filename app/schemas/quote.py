from pydantic import BaseModel, ConfigDict

class MessageResponse(BaseModel):
    """단순 메시지 응답용 스키마 (API 상태 확인, 성공 메시지 등)"""
    message: str

class QuoteResponse(BaseModel):
    """명언 데이터 응답용 스키마 (실제 명언 데이터 반환)"""
    id: int
    content: str
    author: str
    category: str| None = None

    # 사진 속 'Type 변환'의 핵심 설정입니다.
    # 이 설정이 있어야 DB(ORM) 객체를 Pydantic 스키마로 바꿀 수 있어요.
    model_config = ConfigDict(from_attributes=True)