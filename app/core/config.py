# 환경변수
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str = "postgres://사용자명:비밀번호@localhost:5432/db이름"

    # JWT용 비밀키
    SECRET_KEY: str # 기본값을 .env에서 가져올 수 있게 기본값 지정 삭제
    ALGORITHM: str = "HS256"

    #env 파일 읽어오기
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding='utf-8',
        extra='ignore' #다른 변수가 있어도 무시
    )

settings = Settings()

TORTOISE_ORM = {
    "connections": {"default": settings.DATABASE_URL},
    "apps": {
        "models": {
            "models": ["app.models.user", "aerich.models"],
            "default_connection": "default",
        },
    },
}