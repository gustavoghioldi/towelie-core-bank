from django.contrib import admin

from master.models.currency import Currency

# Register your models here.
@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'iso_code' ,'name', 'symbol', )
