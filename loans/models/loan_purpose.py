from operator import index
from django.db import models
from master.models.abstract_model import AbstractModel

class LoanPurpose(AbstractModel):
    name = models.CharField(max_length=25)
    code = models.CharField(max_length=4)
