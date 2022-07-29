from django.db import models
from master.models.abstract_model import AbstractModel
from master.models.country import Country

class Identifier(AbstractModel):
    name = models.CharField(max_length=128)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)