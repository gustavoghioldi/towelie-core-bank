from django.db import models
from master.models.abstract_model import AbstractModel


class LoanSubmitted(AbstractModel):
    at = models.DateTimeField()
    