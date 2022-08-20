from locale import currency
from django.db import models
from master.models.abstract_model import AbstractModel, decimal_field
from master.models.currency import Currency


class Fund(AbstractModel):
    name = models.CharField(max_length=40)
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING)
    principal = decimal_field
    