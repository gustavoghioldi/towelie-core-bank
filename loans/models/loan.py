from django.db import models
from loans.models.loan_purpose import LoanPurpose
from clients.models.client import Client
from master.models.abstract_model import AbstractModel, decimal_field
from loans.models.loan_approved import LoanApproved
from loans.models.loan_submitted import LoanSubmitted
from loans.models.loan_disbursement import LoanDisbursement
from org.models.loan import LoanProduct



class Loan(AbstractModel):
    client              = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    #officer = 
    #channel = 
    #seller  = 
    loan_product         = models.ForeignKey(LoanProduct, on_delete=models.DO_NOTHING)
    loan_prupose         = models.ForeignKey(LoanPurpose, on_delete=models.DO_NOTHING)
    # fund   
    approved             = models.ForeignKey(LoanApproved, on_delete=models.DO_NOTHING, null=True, blank=True)
    submitted            = models.ForeignKey(LoanSubmitted, on_delete=models.DO_NOTHING, null=True, blank=True)
    disbursement         = models.ForeignKey(LoanDisbursement, on_delete=models.DO_NOTHING, null=True, blank=True)
    principal            = decimal_field
    number_of_repayments = models.SmallIntegerField()
    first_repayment_on   = models.DateField()
    
