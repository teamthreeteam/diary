from tortoise import fields, models

class Reflection(models.Model):
    id = fields.IntField(pk=True)
    question_text = fields.TextField()

    class Meta:
        table = "reflection"