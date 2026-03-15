from django.db import models


class FilingFrequency(models.Model):
    code = models.CharField(max_length=20, unique=True)
