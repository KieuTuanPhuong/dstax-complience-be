from django.db import models

from libs.models import BaseModel


class FilingFrequency(BaseModel):
    code = models.CharField(max_length=20, unique=True)
