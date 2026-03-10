from fastapi import FastAPI

app = FastAPI(title="나만의 일기장 API")

@app.get("/")
def read_root():
    return {"message": "Hello! FastAPI 서버가 정상적으로 실행 중입니다."}

# Tortoise ORM을 FastAPI에 등록
register_tortoise(
    app,
    config=TORTOISE_CONFIG,
    generate_schemas=True, # 서버 켤 때 자동으로 테이블 생성 (연습용)
    add_exception_handlers=True,
)