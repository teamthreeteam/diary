# app/core/config.py (또는 database.py)
TORTOISE_ORM = {
    "connections": {"default": "postgres://사용자명:비밀번호@localhost:5432/db이름"},
    "apps": {
        "models": {
            "models": ["app.models.user", "aerich.models"], # 내 모델들 위치
            "default_connection": "default",
        },
    },
}