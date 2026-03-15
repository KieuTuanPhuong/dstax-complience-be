from django.db import models


class PrepaymentMethod(models.Model):
    jurisdiction = models.OneToOneField("Jurisdiction", on_delete=models.CASCADE)
    method_description = models.CharField(max_length=255)
