from django.db import models

from libs.models import BaseModel


class FilingType(BaseModel):
    name = models.CharField(max_length=50, unique=True)
