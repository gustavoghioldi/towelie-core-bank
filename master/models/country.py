from django.db import models

from master.models.abstract_model import AbstractModel

class Country(AbstractModel):
    name     = models.CharField(max_length=64)
    iso_code = models.CharField(max_length=2, unique=True)