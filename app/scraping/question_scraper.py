import requests
from bs4 import BeautifulSoup
from tortoise import Tortoise, run_async
from app.db.database import TORTOISE_CONFIG
from app.models.reflection import Reflection

# 하드코딩된 질문 목록
QUESTIONS = [
    "내가 느끼는 나이와 실제 나이가 일치하는가?",
    "삶이 짧다고 느낀다면, 왜 좋아하지 않는 일은 하면서 좋아하는 일은 미루는가?",
    "종합적으로 나는 말과 행동 중 어떤 일에 더 집중했는가?",
    "나는 할 일을 잘하는 것과 옳은 일을 해야 하는 것 중 어떤 것을 더 고민하는가?",
    "세상의 단 한 가지를 바꿀 수 있다면 무엇을 바꾸겠는가?",
    "만약 행복이 돈이라면, 부유해지기 위해 어떤 일을 하겠는가?",
    "내가 좋아하는 일과 해야 하는 일 중 어떤 것을 위해 노력하는가?",
    "내 삶을 어느 정도 통제하고 있는가?",
    "내가 존경하는 사람이 나를 불친절하게, 혹은 불공평하게 비난한다면 어쩌겠는가?",
    "한 사람의 삶을 바꾸기 위한 조언을 한 가지 할 수 있다면 무슨 말을 하겠는가?",
    "역사상 얼마나 많은 천재들이 처음에는 미치광이로 여겨졌는가?",
    "걱정 많은 천재와 팔자 좋은 바보 중 어떤 것을 선호하는가?",
    "남들이 모르는 일 중 할 줄 아는 일은 무엇인가?",
    "내가 하고 싶지만 아직까지 이루지 못한 일은 무엇인가? 무엇이 나를 막고 있는가?",
    "내가 전진할 수 없게 막는 것 중 내가 붙잡고 있는 것은 무엇인가?",
    "과거에 어떤 일이 있었는지가 과연 중요한가?",
    "나는 왜 나일까?",
    "나는 내가 친구로 삼을만한 사람인가?",
    "삶에서 내가 가장 감사하는 일은 무엇인가?",
    "내 유년기 중 가장 행복했던 기억은 무엇인가? 이유는 뭔가?",
    "지금 아니라면, 언제인가?",
    "내가 꿈꾸고 있는 것을 아직 이루지 않았다면, 무엇 때문인가?",
    "기다리겠는가, 아니면 지금 당장 행동 할 것인가?",
    "오늘 같은 날을 수백 번 겪은 것 같은 기분인가?",
    "만약 내일 세상이 멸망한다면, 오늘 누구와 시간을 보내겠는가?",
    "유명하거나 잘생겨지기 위해 몇 년을 포기할 수 있는가?",
    "삶을 사는 것과 목숨이 붙어있는 것의 차이는 무엇인가?",
    "만약 실수로부터 배울 수 있다고 생각한다면, 왜 실패를 두려워하는가?",
    "나 자신 외에 아무도 나를 판단하지 않는다면 어떻게 행동하겠는가?",
    "나는 내 스스로 결정을 내리는가, 남이 내린 결정을 따르는가?",
]

async def save_questions_to_db(questions: list[str]):
    await Tortoise.init(config=TORTOISE_CONFIG)
    await Tortoise.generate_schemas()

    saved = 0
    for q in questions:
        _, created = await Reflection.get_or_create(question_text=q)
        if created:
            saved += 1

    print(f"{saved}개 질문 DB 저장 완료! (중복 제외)")
    await Tortoise.close_connections()

async def main():
    print(f"총 {len(QUESTIONS)}개 질문 DB 저장 시작...")
    await save_questions_to_db(QUESTIONS)


if __name__ == "__main__":
    run_async(main())
