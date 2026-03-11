from tortoise import fields, models

class Diary(models.Model):
    id = fields.IntField(pk=True)
    # User와 1:N 관계 (작성자)
    user = fields.ForeignKeyField("models.User", related_name="diaries")
    title = fields.CharField(max_length=255)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "diaries"