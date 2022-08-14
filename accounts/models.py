from django.db import models
from accounts.tasks.account_ledger_receiver import account_ledger_receiver_post_save, account_ledger_receiver_pre_save
from clients.models.client import Client
from org.models.account import AccountProduct
from master.models.abstract_model import AbstractModel, decimal_field

class AccountLedgerChangeType(models.TextChoices):
    DEBIT  = "DEBIT"
    CREDIT = "CREDIT"

class ClientAccount(AbstractModel):
    client  = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    account = models.ForeignKey(AccountProduct, on_delete=models.DO_NOTHING, related_name='client_account_account')

class ClientAccountLedger(AbstractModel):
    client_account = models.ForeignKey(ClientAccount, on_delete=models.DO_NOTHING)
    account_ledger_change_type = models.CharField(max_length=128, choices=AccountLedgerChangeType.choices) 
    account_ledger_change_reason = models.CharField(max_length=24)
    amount = decimal_field
    comment = models.TextField()

# class FundAccount(models.Model):
    # client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    
models.signals.pre_save.connect(sender=ClientAccountLedger, receiver=account_ledger_receiver_pre_save)
models.signals.post_save.connect(sender=ClientAccountLedger, receiver=account_ledger_receiver_post_save)
