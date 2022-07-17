from tabnanny import verbose
from django.db import models

class Currency(models.Model):
    name     = models.CharField(max_length=24)
    iso_code = models.CharField(max_length=3)
    code     = models.CharField(max_length=3, default="$")

    class Meta:
        verbose_name_plural = "Currencies"