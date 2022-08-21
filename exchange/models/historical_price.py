from django.db import models
from master.models.abstract_model import AbstractModel, decimal_field
from master.models.currency import Currency

class HistoricalPrice(AbstractModel):
    source = models.CharField(max_length=64)
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING, related_name='currency')
    reference_currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING, related_name='reference_currency')
    price = decimal_field
    last_datetime = models.DateTimeField(auto_now=True) 

    @property
    def price(self):
        return self.price
