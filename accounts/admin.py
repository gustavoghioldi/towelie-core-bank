from django.contrib import admin

from accounts.models import ClientAccountLedger, ClientAccount

@admin.register(ClientAccount)
class ClientAccountAdmin(admin.ModelAdmin):
    pass

@admin.register(ClientAccountLedger)
class ClientAccountLedgerAdmin(admin.ModelAdmin):
    pass