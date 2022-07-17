from django.db import models
from master.models.currency import Currency

class AccountProduct(models.Model):
    name = models.CharField(max_length=24)
    shot_name = models.CharField(max_length=6)
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING) 
    
