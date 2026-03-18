from django.db import models

from libs.models import BaseModel


class JurisdictionLevel(BaseModel):
    name = models.CharField(max_length=50, unique=True)
