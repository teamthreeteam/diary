import httpx
from bs4 import BeautifulSoup

async def get_quotes_from_web():
    """웹 사이트에서 명언 데이터를 스크래핑합니다."""
    url = "https://quotes.toscrape.com/"
    # 브라우저처럼 보이게 하여 차단을 방지합니다.
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    async with httpx.AsyncClient(headers=headers) as client:
        try:
            response = await client.get(url)
            if response.status_code != 200:
                return []

            soup = BeautifulSoup(response.text, "html.parser")
            quote_blocks = soup.select("div.quote")
            
            scraped_data = []
            for block in quote_blocks:
                # 데이터 추출 및 공백 제거
                content = block.select_one("span.text").text.strip()
                author = block.select_one("small.author").text.strip()
                # 첫 번째 태그를 카테고리로 사용, 없을 경우 General
                tag_element = block.select_one("div.tags a.tag")
                category = tag_element.text if tag_element else "General"
                
                scraped_data.append({
                    "content": content,
                    "author": author,
                    "category": category
                })
            return scraped_data
        except Exception as e:
            print(f"스크래핑 중 오류 발생: {e}")
            return []