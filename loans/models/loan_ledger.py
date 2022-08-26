from loans.models.loan import Loan
from master.models.abstract_model import AbstractModel
from django.db import models

class LoanLedger(AbstractModel):
    loan = models.ForeignKey(Loan, on_delete=models.DO_NOTHING)
    payment = models.SmallIntegerField()
    payment_date = models.DateField()
    payment_amount =  models.DecimalField(max_digits=48, decimal_places=16, default=0.0)
    paid_out = models.BooleanField(default=False)