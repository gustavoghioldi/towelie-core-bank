from django.contrib import admin
from exchange.models.historical_price import HistoricalPrice
# Register your models here.
@admin.register(HistoricalPrice)
class HistoricalPriceAdmin(admin.ModelAdmin):
    list_display = ( 'source','curreny', 'reference_currency', 'price' )