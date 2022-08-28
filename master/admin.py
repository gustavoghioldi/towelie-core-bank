from django.contrib import admin

from master.models.country import Country
from master.models.currency import Currency
from master.models.identifier import Identifier

# Register your models here.
@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('iso_code' ,'name', 'symbol', )
    
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(Identifier)
class IdentifierAdmin(admin.ModelAdmin):
    pass    
