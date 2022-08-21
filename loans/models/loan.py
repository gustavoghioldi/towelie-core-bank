from django.db import models
from loans.models.loan_purpose import LoanPurpose
from clients.models.client import Client
from master.models.abstract_model import AbstractModel, decimal_field
from loans.models.loan_approved import LoanApproved
from loans.models.loan_submitted import LoanSubmitted
from loans.models.loan_disbursement import LoanDisbursement
from org.models.loan import LoanProduct
from django.core.exceptions import ValidationError


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
    
    def clean(self) -> None:
        self._validation_errors()
        return super().clean()

    def save(self, *args, **kwargs):
        self._validation_errors()
        super().save(*args, **kwargs)

    def _validation_errors (self):
        #validar cantidad de cuotas maximas
        if self.loan_product.repayments_max < self.number_of_repayments:
            raise ValidationError(f'Max repayments for {self.loan_product.name} is {self.loan_product.repayments_max} repayment')
        #validar cantidad minima de cuotas
        if self.loan_product.repayments_min > self.number_of_repayments:
            raise ValidationError(f'Min repayments for {self.loan_product.name} is {self.loan_product.repayments_min} repayment')

        # valirar max amount
        # valiar min amount    