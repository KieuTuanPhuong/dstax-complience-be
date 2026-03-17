from django.db import models

from libs.models import BaseModel


class LegalEntity(BaseModel):
    client = models.ForeignKey("Client", on_delete=models.CASCADE, related_name="legal_entities")
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
