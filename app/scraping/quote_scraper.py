import httpx
from bs4 import BeautifulSoup

SOURCE_URL = "https://quotes.toscrape.com/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

async def scrape_quotes():
    async with httpx.AsyncClient(headers=HEADERS) as client: # 헤더를 반드시 포함!
        response = await client.get(SOURCE_URL)
        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        quote_elements = soup.select("div.quote")

        results = []
        for el in quote_elements:
            results.append({
                "text": el.select_one("span.text").get_text(strip=True),
                "author": el.select_one("small.author").get_text(strip=True)
            })
        return results
