from django.db import models

from master.models.abstract_model import AbstractModel

class Country(models.Model):
    name     = models.CharField(max_length=64)
    iso_code = models.CharField(max_length=2, primary_key=True)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.iso_code