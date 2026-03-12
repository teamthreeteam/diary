# 환경변수
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str = "postgres://사용자명:비밀번호@localhost:5432/db이름"

    # JWT용 비밀키
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"

    #env 파일 읽어오기
    model_config = SettingsConfigDict(env_file=".env")

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