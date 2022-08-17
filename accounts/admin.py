from django.contrib import admin

from accounts.models import ClientAccountLedger, ClientAccount
from accounts.forms.admin.client_account_ledger_form import ClientAccountLedgerForm
@admin.register(ClientAccount)
class ClientAccountAdmin(admin.ModelAdmin):
    list_display = ('client', 'account', 'balance', )

@admin.register(ClientAccountLedger)
class ClientAccountLedgerAdmin(admin.ModelAdmin):
    form = ClientAccountLedgerForm
    list_display = ('client_account', 'account_ledger_change_type', 'balance', )