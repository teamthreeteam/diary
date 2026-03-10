from tortoise import fields, models

class TokenBlacklist(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="blacklisted_tokens")
    token = fields.TextField()
    expires_at = fields.DatetimeField()
    logout_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "token_blacklist"