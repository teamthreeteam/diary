# app/db/database.py
import os
from dotenv import load_dotenv

load_dotenv()

TORTOISE_CONFIG = {
    "connections": {"default": os.getenv("DATABASE_URL")},
    "apps": {
        "models": {
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