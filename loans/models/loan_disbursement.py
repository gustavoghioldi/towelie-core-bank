from django.db import models
from master.models.abstract_model import AbstractModel

class LoanDisbursement(AbstractModel):
    at = models.DateTimeField()