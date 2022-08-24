from tkinter.tix import Balloon
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
    default_collector = models.BooleanField(default=False)
    overdraw = models.DecimalField(max_digits=48, decimal_places=16, default=0.0)

    def clean(self) -> None:
        self._validation_errors()
        return super().clean()
        
    def save(self, *args, **kwargs):
        self._validation_errors()
        super().save(*args, **kwargs)

    def _validation_errors(self):
        #valida que la cuenta pueda ser recaudadora
        if self.default_collector and not self.account.collector:
            raise ValidationError(f"{self.account} isn`t collector account product")
        #valida que el monto maximo de sobregiro este permitido en este tipo de cuentas
        if self.account.max_overdraw < self.overdraw:
            raise ValidationError(f"{self.account} max overdraw is {float(self.account.max_overdraw)} ")     
            
class ClientAccountLedger(AbstractModel):
    client_account = models.ForeignKey(ClientAccount, on_delete=models.DO_NOTHING)
    account_ledger_change_type = models.CharField(max_length=128, choices=AccountLedgerChangeType.choices) 
    account_ledger_change_reason = models.CharField(max_length=24)
    amount = decimal_field
    comment = models.TextField(null=True, blank=True)

    def clean(self):
        if self.account_ledger_change_type == 'DEBIT':
            if self.client_account.balance - self.balance < self.client_account.overdraw:
                raise ValidationError(f"the account balance cannot be less than 0, currently it is {self.client_account.balance }")
            super(ClientAccountLedger, self).clean()

# class FundAccount(models.Model):
    # client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
