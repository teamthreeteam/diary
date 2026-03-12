from fastapi import APIRouter, HTTPException
from app.services import quote_service
from app.schemas.quote import QuoteResponse, MessageResponse # 스키마 임포트

router = APIRouter(prefix="/quotes", tags=["Quotes"])

@router.get("/", response_model=MessageResponse, summary="명언 API 상태 확인")
async def get_quotes():
    # 1. JSON 문자열을 파이썬 dict로 인식한 뒤, 
    # 2. MessageResponse 스키마 객체로 변환하여 반환
    return MessageResponse(message="quotes list is ready")

@router.post("/sync", response_model=MessageResponse, summary="외부 사이트 명언 데이터 동기화")
async def sync_quotes():
    # 서비스 계층에서 비즈니스 로직 처리
    result = await quote_service.sync_quotes_to_db()
    
    # 처리 결과를 스키마에 담아 반환 (API 단에서 ORM이나 생 데이터를 노출하지 않음)
    return MessageResponse(message=f"Sync completed: {result}")

@router.get("/random", response_model=QuoteResponse, summary="오늘의 랜덤 명언 조회")
async def get_random_quote():
    # 1. 서비스에서 DB 데이터(ORM 객체)를 가져옴
    quote_orm = await quote_service.get_random_quote()
    
    if not quote_orm:
        raise HTTPException(status_code=404, detail="저장된 명언이 없습니다.")
    
    # 2. [핵심] ORM 객체를 스키마 틀에 넣어서 '순수한 데이터 타입'으로 변환
    # 이 과정을 통해 API 레이어에서 ORM 모델의 의존성을 제거합니다.
    return QuoteResponse.model_validate(quote_orm)