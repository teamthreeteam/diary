from tortoise import fields, models

class Quote(models.Model):
    id = fields.IntField(pk=True)
    author = fields.CharField(max_length=100)
    content = fields.TextField()
    category = fields.CharField(max_length=50)

    class Meta:
        table = "quotes"