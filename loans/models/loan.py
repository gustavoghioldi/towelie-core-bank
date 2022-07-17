from django.db import models
from loans.models.loan_purpose import LoanPurpose
from clients.models.client import Client
from master.models.abstract_model import AbstractModel, decimal_field



class Loan(AbstractModel):
    client  = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    #officer = 
    #channel = 
    #seller  =
    loan_prupose = models.ForeignKey(LoanPurpose, on_delete=models.DO_NOTHING)
    # fund
    approved = models.BooleanField()
    submitted_on = models.DateField()
    disbursement_on = models.DateField()
    principal       = decimal_field
    number_of_repayments = models.SmallIntegerField()
    first_repayment_on = models.DateField()
    
