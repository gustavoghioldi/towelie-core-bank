from django.contrib import admin
from exchange.models.historical_price import HistoricalPrice


@admin.register(HistoricalPrice)
class HistoricalPriceAdmin(admin.ModelAdmin):
    list_display = ('source', 'currency', 'reference_currency', 'price' )
