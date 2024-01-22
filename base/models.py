from django.db import models

import uuid

class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key = True,editable = False , default=uuid.uuid4)
    create_at = models.DateTimeField(auto_now_add =True)
    update_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract =True