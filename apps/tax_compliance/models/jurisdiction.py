from django.db import models

from libs.models import BaseModel


class Jurisdiction(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    level = models.ForeignKey("JurisdictionLevel", on_delete=models.PROTECT)
    due_date_time = models.DateTimeField(null=True)
