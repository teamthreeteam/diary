from tortoise import fields, models

class UserQuestionHistory(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="question_histories")
    question = fields.ForeignKeyField("models.Reflection", related_name="user_histories")
    # 다이어리와 1:1 연결 (선택사항이므로 null=True)
    diary = fields.ForeignKeyField("models.Diary", related_name="question_history", null=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "user_question_histories"