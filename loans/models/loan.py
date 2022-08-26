from django.db import models
from loans.models.loan_purpose import LoanPurpose
from clients.models.client import Client
from master.models.abstract_model import AbstractModel
from org.models.loan import LoanProduct
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class LoanCycleLifeStatus(models.TextChoices):
    SUBMITTED = 'SUBMITTED'
    APPROVED = 'APPROVED'
    DISBURSED = 'DISBURSED'

class Loan(AbstractModel):
    client              = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    #officer = 
    #channel = 
    #seller  = 
    loan_product         = models.ForeignKey(LoanProduct, on_delete=models.DO_NOTHING)
    loan_prupose         = models.ForeignKey(LoanPurpose, on_delete=models.DO_NOTHING)
    # fund    
    status               = models.CharField(choices=LoanCycleLifeStatus.choices,
                              max_length=16, 
                              default=LoanCycleLifeStatus.SUBMITTED.value,
                              null=True, 
                              blank=True)
    principal            = models.DecimalField(max_digits=48, decimal_places=16, default=0.0)
    number_of_repayments = models.SmallIntegerField()
    first_repayment_on   = models.DateField()
    subimtted_by         = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    
    def __str__(self):
        return str(self.uuid)

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
        # validar maxio credito del cliente
        # valirar min amount
        if self.loan_product.principal_min > self.principal:
            raise ValidationError(f'Min principal for {self.loan_product.name} is {self.loan_product.principal_min}')
        # valiar max amount
        if self.loan_product.principal_max < self.principal:
            raise ValidationError(f'Max principal for {self.loan_product.name} is {self.loan_product.principal_max}')
        # validar si el cliente esta activo
        if not self.client.activation_date:
            raise ValidationError(f'Client {self.client.user.username} is not active')
                        