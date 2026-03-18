from django.db import models

from libs.models import BaseModel


class TaxType(BaseModel):
    name = models.CharField(max_length=100, unique=True)
