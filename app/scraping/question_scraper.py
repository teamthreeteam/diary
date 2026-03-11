import requests
from bs4 import BeautifulSoup
from tortoise import Tortoise, run_async
from app.models.userquestionhistory import Question
from app.db.database import TORTOISE_ORM

URLS = [
    "https://wonderfulmind.co.kr/self-growth-ask-30-questions/",
]


def scrape_questions() -> list[str]:
    questions = []
    headers = {"User-Agent": "Mozilla/5.0"}

    for url in URLS:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        article = (
            soup.select_one(".entry-content")
            or soup.select_one("article")
            or soup.find("body")
        )

        if not article:
            print(f"본문 영역을 찾을 수 없습니다: {url}")
            continue

        items = article.select("ol li")

        for item in items:
            for a_tag in item.find_all("a"):
                a_tag.replace_with(a_tag.get_text())

            text = item.get_text(strip=True)

            if not text or len(text) < 5:
                continue

            questions.append(text)

        print(f"✓ {url} → {len(items)}개 질문 수집")

    questions = list(dict.fromkeys(questions))
    print(f"\n총 {len(questions)}개 질문 수집 완료!")
    return questions


async def save_questions_to_db(questions: list[str]):
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()

    saved = 0
    for q in questions:
        _, created = await Question.get_or_create(question_text=q)
        if created:
            saved += 1

    print(f"{saved}개 질문 DB 저장 완료! (중복 제외)")
    await Tortoise.close_connections()


async def main():
    print("질문 스크래핑 시작...\n")
    questions = scrape_questions()

    if questions:
        print("\n수집된 질문 목록:")
        for i, q in enumerate(questions, 1):
            print(f"  {i}. {q}")
        print("\nDB 저장 중...")
        await save_questions_to_db(questions)
    else:
        print("수집된 질문이 없습니다.")


if __name__ == "__main__":
    run_async(main())
