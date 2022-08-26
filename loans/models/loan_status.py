from master.models.abstract_model import AbstractModel
from loans.models.loan import Loan
from django.db import models
from django.contrib.auth.models import User

class Disbursed(AbstractModel):
    loan = models.ForeignKey(Loan, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    note = models.TextField()
    
class Approved(AbstractModel):
    loan = models.ForeignKey(Loan, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    note = models.TextField()