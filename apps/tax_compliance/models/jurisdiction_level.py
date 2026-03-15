from django.db import models


class JurisdictionLevel(models.Model):
    name = models.CharField(max_length=50, unique=True)
