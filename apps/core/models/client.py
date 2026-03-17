from django.db import models

from libs.models import BaseModel


class Client(BaseModel):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
