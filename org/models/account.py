from django.db import models
from master.models.currency import Currency
from master.models.abstract_model import AbstractModel, decimal_field

class AccountProduct(AbstractModel):
    name              = models.CharField(max_length=24)
    short_name        = models.CharField(max_length=6)
    currency          = models.ForeignKey(Currency, on_delete=models.DO_NOTHING)
    default_overdraw  = models.DecimalField(max_digits=48, decimal_places=16, default=0.0)
    max_overdraw      = models.DecimalField(max_digits=48, decimal_places=16, default=0.0)
    collector      = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name