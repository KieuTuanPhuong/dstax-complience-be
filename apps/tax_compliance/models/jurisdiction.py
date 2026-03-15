from django.db import models


class Jurisdiction(models.Model):
    name = models.CharField(max_length=255, unique=True)
    level = models.ForeignKey("JurisdictionLevel", on_delete=models.PROTECT)
    due_date_time = models.DateTimeField(null=True)
