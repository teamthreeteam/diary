import httpx
from bs4 import BeautifulSoup
import random
from app.models.quote import Quote

async def sync_quotes_to_db():
    """quotes.toscrape.com에서 명언을 긁어와 DB에 저장합니다."""
    url = "https://quotes.toscrape.com/"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    async with httpx.AsyncClient(headers=headers) as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            # 명언 하나하나를 감싸고 있는 div.quote 태그들을 찾습니다.
            quote_elements = soup.select('div.quote')
            
            new_quotes_count = 0
            for elem in quote_elements:
                # 명언 내용과 저자 추출
                content = elem.select_one('span.text').get_text().strip()
                author = elem.select_one('small.author').get_text().strip()

                ## Tortoise ORM으로 저장 (중복 방지: 내용이 같으면 생성하지 않음)
                # content는 큰 따옴표로 감싸져 올 수 있으니 필요시 처리
                await Quote.get_or_create(
                    content=content.replace('“', '').replace('”', ''),
                    defaults={"author": author}
                )
                new_quotes_count += 1
                
            return {"status": "success", "message": f"{new_quotes_count}개의 명언을 성공적으로 가져왔습니다."}
            
        except Exception as e:
            return {"status": "error", "message": f"스크래핑 중 오류 발생: {str(e)}"}

async def get_random_quote():
    """DB에서 랜덤하게 명언 한 건을 가져옵니다."""
    count = await Quote.all().count()
    if count == 0:
        return None
    
    random_index = random.randint(0, count - 1)
    return await Quote.all().offset(random_index).first()