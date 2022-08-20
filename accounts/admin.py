from django.contrib import admin

from accounts.models import ClientAccountLedger, ClientAccount
from accounts.forms.admin.client_account_ledger_form import ClientAccountLedgerForm
@admin.register(ClientAccount)
class ClientAccountAdmin(admin.ModelAdmin):
    list_display = ('uuid','get_client', 'get_account', 'get_currency_name','get_balance', )
    list_filter = ('account__name', 'account__currency__name', )

    @admin.display(description="client")
    def get_client(self, obj):
        return obj.client.user.username

    @admin.display(description="account name")
    def get_account(self, obj):
        return obj.account.name

    @admin.display(description="currency")
    def get_currency_name(self, obj):
        return obj.account.currency.name    

    @admin.display(description="balance")
    def get_balance(self, obj):
        return f'{obj.account.currency.symbol} {round(obj.balance, obj.account.currency.decimal_places)}'   

@admin.register(ClientAccountLedger)
class ClientAccountLedgerAdmin(admin.ModelAdmin):
    form = ClientAccountLedgerForm
    list_display = ('client_account', 'account_ledger_change_type', 'balance', )