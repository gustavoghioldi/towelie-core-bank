from django.db import models

from master.models.abstract_model import AbstractModel

class Office(AbstractModel):
    name = models.CharField(max_length=50)
    opening_date = models.DateField()
    