from django.db import models

from libs.models import BaseModel


class PrepaymentMethod(BaseModel):
    jurisdiction = models.OneToOneField("Jurisdiction", on_delete=models.CASCADE)
    method_description = models.CharField(max_length=255)
