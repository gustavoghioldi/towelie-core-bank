from django.db import models
from master.models.abstract_model import AbstractModel

class LoanApproved(AbstractModel):
    at = models.DateTimeField()