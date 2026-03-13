from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.api.routers import question, quote, diary
from app.api.routers.auth import router as auth_router
from app.core.config import TORTOISE_ORM

app = FastAPI(title="나만의 일기장 API")

# 라우터 등록
app.include_router(question.router)
app.include_router(quote.router)
app.include_router(diary.router)

@app.get("/")
def read_root():
    return {"message": "서버가 정상적으로 작동 중입니다!"}

app.include_router(auth_router, prefix="/api/v1/auth", tags=["인증"])

register_tortoise(
    app,
    # db_url="sqlite://sql_app.db", # DB 파일명
    # config=TORTOISE_CONFIG, # 재확인!!!
    config = TORTOISE_ORM, #app/core/config.py에 맞춘 db 연결 방식입니다!
    modules={
        "models": [
            "app.models.user",               # 1. 유저가 가장 기본
            "app.models.reflection",         # 2. 질문 데이터
            "app.models.quote",              # 3. 명언 데이터
            "app.models.diary",              # 4. 일기 데이터는 유저와 질문을 참조
            "app.models.bookmark",           # 5. 즐겨찾기 데이터
            "app.models.userquestionhistory" # 6. 기록은 유저와 질문을 참조
        ]
    },
    generate_schemas=True, # 서버 켤 때 테이블 없으면 자동 생성
    add_exception_handlers=True)