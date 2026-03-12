import random
from app.scraping import quote_scraper
from app.models.quote import Quote
from app.schemas.quote import QuoteResponse

async def get_random_quote():
    """
    [역할] DB에서 랜덤하게 명언 하나를 가져와 반환
    라우터(quote.py)에서 이 함수를 기다리고 있습니다.
    """
    # 1. 전체 명언 개수 확인
    count = await Quote.all().count()
    if count == 0:
        return None
    
    # 2. 무작위 위치(offset) 계산 후 하나 가져오기
    offset = random.randint(0, count - 1)
    return await Quote.all().offset(offset).first()

async def sync_quotes_to_db():
    """
    [역할] 스크래퍼를 통해 데이터를 가져와 검증 후 DB 저장
    """
    # 1. 스크래퍼 호출 (Python 데이터 가져오기)
    raw_data = await quote_scraper.scrape_quotes()
    
    saved_count = 0
    for item in raw_data:
        try:
            # 2. 스키마로 검증 (Schema 단계 - 핵심!)
            validated_data = QuoteResponse(
                id=0,
                author=item["author"],
                content=item["text"]
            )
            
            # 3. DB 저장 (ORM 단계)
            exists = await Quote.filter(content=validated_data.content).exists()
            if not exists:
                await Quote.create(
                    author=validated_data.author,
                    content=validated_data.content
                )
                saved_count += 1
        except Exception as e:
            # 에러 확인
            print(f"Sync 에러 발생: {e}")
            continue
    return saved_count