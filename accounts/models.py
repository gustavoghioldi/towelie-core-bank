from django.db import models
from clients.models.client import Client
from org.models.account import AccountProduct
from master.models.abstract_model import AbstractModel, decimal_field
from django.core.exceptions import ValidationError
class AccountLedgerChangeType(models.TextChoices):
    DEBIT  = "DEBIT"
    CREDIT = "CREDIT"

class ClientAccount(AbstractModel):
    client  = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    account = models.ForeignKey(AccountProduct, on_delete=models.DO_NOTHING, related_name='client_account_account')
    balance = decimal_field

class ClientAccountLedger(AbstractModel):
    client_account = models.ForeignKey(ClientAccount, on_delete=models.DO_NOTHING)
    account_ledger_change_type = models.CharField(max_length=128, choices=AccountLedgerChangeType.choices) 
    account_ledger_change_reason = models.CharField(max_length=24)
    amount = decimal_field
    comment = models.TextField()

    def clean(self):
        if self.client_account.balance - self.balance < 0:
            raise ValidationError(f"the account balance cannot be less than 0, currently it is {self.client_account.balance }")
        super(ClientAccountLedger, self).clean()

# class FundAccount(models.Model):
    # client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
