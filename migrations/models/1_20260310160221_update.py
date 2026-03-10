from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "quotes" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "author" VARCHAR(100) NOT NULL,
    "content" TEXT NOT NULL,
    "category" VARCHAR(50) NOT NULL
);
        CREATE TABLE IF NOT EXISTS "bookmarks" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "quote_id" INT NOT NULL REFERENCES "quotes" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
        CREATE TABLE IF NOT EXISTS "diaries" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(255) NOT NULL,
    "content" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
        CREATE TABLE IF NOT EXISTS "questions" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "question_text" TEXT NOT NULL
);
        CREATE TABLE IF NOT EXISTS "user_questions" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "diary_id" INT REFERENCES "diaries" ("id") ON DELETE CASCADE,
    "question_id" INT NOT NULL REFERENCES "questions" ("id") ON DELETE CASCADE,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
        ALTER TABLE "users" ALTER COLUMN "nickname" SET NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" ALTER COLUMN "nickname" DROP NOT NULL;
        DROP TABLE IF EXISTS "user_questions";
        DROP TABLE IF EXISTS "diaries";
        DROP TABLE IF EXISTS "questions";
        DROP TABLE IF EXISTS "quotes";
        DROP TABLE IF EXISTS "bookmarks";"""


MODELS_STATE = (
    "eJztW1tz0zoQ/iuZPJWZwpScFhjekjY9LdAEWnNgYBiPYquOJrYUbJk2w+S/H0m+Xxvn0l"
    "it3pLVrqz9JO9+K8l/uw4xoe29+upBt/u+87eLgQPZj4z8sNMF83ki5QIKJrZQ9JmGkICJ"
    "R11gUCa8BbYHmciEnuGiOUUEMyn2bZsLicEUEbYSkY/Rbx/qlFiQTsVAfv5iYoRNeA+96O"
    "98pt8iaJuZcSKTP1vIdbqYC9klpudCkT9tohvE9h2cKM8XdEpwrI0w5VILYugCCnn31PX5"
    "8PnoQjcjj4KRJirBEFM2JrwFvk1T7q6IgUEwx4+NxhMOWvwpL3uvj98ev/vnzfE7piJGEk"
    "veLgP3Et8DQ4HASOsuRTugINAQMCa4QQcguwjd6RS45djFBjn42KDz8EVg7RU/B9zrNsQW"
    "nXLQTk5q0Pqvf3160b8+YFovuC+ELeNgcY/Cpl7QxiFNIJwDz7sjbskCrEYxbbMdICNBgm"
    "Ty9kkDJUbGTPxuAGXaRk4oT45WQPLkqBJI3pTF0XAh91cHtIjkGWuhyIHlaGYtc3iaoemr"
    "6EdL0WU+mGNsL8JwUoOudnk1vNH6V5+5J47n/bYFRH1tyFt6QrrISQ/e5GYi7qTz7VK76P"
    "C/nR/j0VAgSDxqueKJiZ72o8vHBHxKdEzudGCmIl8kjYBZ8px3O0tFby6YAGN2B1xTz7Qk"
    "K2BCyMwB7swrLoBBaHr+8RraQIBbnOow7w/Cbto50cto9UbSZMITJEwEXAQ3xOGMdbKQGI"
    "SJzZy1kcdfbUpmEG+Ih8b7GESdSgwMG4zHO9anzA+y+ULhRPlL2OeF6FK2ZcOjC+mRqnhT"
    "bHJ6Tl4CMLDEqPmz+ZNCdPrQRca0W1JghC2HdSUGSHRUjbHNfLnjGuMPqwzDl2ZVUpcykZ"
    "PT7YQe81ejAYihupwAvj5ahRUzrUoARVuOFxNMIS4hxR9uxqMKQpyY5ID8ipmDP01k0MMO"
    "z4K/2glrDYrc6wzxjcA7uOp/z+N6+mk8yDNa3sGAYdyAou4yvcRstSTBpJlsdYrJ0GaVZW"
    "TKMqrmfUI1b5aiEwr1Rq9F2uThl6MlM7iV9yOBjW/IN0MtZfGcQCskryyGRQDPiQuRhT/C"
    "hcDxko0IYKNsAzJ3etI+/KqqQCZ2wV2cndJLg7nHnII0IJ/9m9P+2bBbfGG3ANuXqB95cU"
    "sHonLg9sOUgv2sEpoUb3RVc6TUhppiSG0LZnUMiSJqNzpaiQ3kLCF3UoNXlpAavK9YgtUl"
    "ZGuBrKOPw+9afdEYs8dP49G/kXq+klQHVs+CvPtzc82JzVqqid3rxBbOTVR1oaqLx6suVj"
    "nxzp3kLfZxjhc61wKId3qMFxRmJdVDXLFVVw+iIlLFg3TFA0sGU1ISrmqOn2ILWVjvPk+g"
    "VPmwSfnAvLdKY3718kzbyILrLu4NqutlLcutAekoT69h2wMZNtBSSVa6JBtzWMqyQZMcUT"
    "CUJaI9RqZYK8KJmkRdCnyEiJe7S1oS94q3Taujn7jdqk8yyioGShQDxQQ2iX2xgYp55ewY"
    "3s+RC7019mCzlnLuwUqy5xq5XbubbhOL+HSNicwYyjmPT2YvveSQRG2mq830Fmym75LllX"
    "Hgig/NS6hy/Xfnuip5paV76uT/iSY1fk1s0SyrpU3WSmuPf/627Vu78UZOw/vOGavnRAkU"
    "j1I8qg1XnpOd+Y1vPSddyYteLiI9jKAZXTzeEL5Vv9Rvz1WNPHTpLLh/Br/8H7OY7Mk="
)
