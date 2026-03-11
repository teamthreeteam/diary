from fastapi import APIRouter, HTTPException
from app.services import quote_service
from app.schemas.quote import QuoteResponse

router = APIRouter(prefix="/quotes", tags=["Quotes"])

@router.get("/", summary="명언 API 상태 확인")
async def get_quotes():
    return {"message": "quotes list is ready"}

@router.post("/sync", summary="외부 사이트 명언 데이터 동기화")
async def sync_quotes():
    # 스크래핑 후 DB 저장
    result = await quote_service.sync_quotes_to_db()
    return result

@router.get("/random", response_model=QuoteResponse, summary="오늘의 랜덤 명언 조회")
async def get_random_quote():
    quote = await quote_service.get_random_quote()
    if not quote:
        ## 데이터가 없을 때 404를 던집니다.
        raise HTTPException(status_code=404, detail="저장된 명언이 없습니다. /sync를 먼저 호출하세요.")
    return quote