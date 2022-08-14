from django.db import models
from master.models.currency import Currency
from master.models.abstract_model import AbstractModel

class AccountProduct(AbstractModel):
    name = models.CharField(max_length=24)
    shot_name = models.CharField(max_length=6)
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING)