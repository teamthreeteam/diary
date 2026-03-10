from tortoise import fields, models

class Bookmark(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="bookmarks")
    quote = fields.ForeignKeyField("models.Quote", related_name="bookmarks")
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "bookmarks"