# app/db/database.py
import os
from dotenv import load_dotenv

load_dotenv()

TORTOISE_CONFIG = {
    "connections": {"default": os.getenv("DATABASE_URL")},
    "apps": {
        "models": {
            # 여기에 모든 모델 파일 경로를 적어줍니다.
            "models": [
                "app.models.user",
                "aerich.models",
                "app.models.bookmark",
                "app.models.diary",
                "app.models.quote",
                "app.models.reflection",
                "app.models.tokenblacklist",
                "app.models.userquestionhistory"
            ],
            "default_connection": "default",
        },
    },
}