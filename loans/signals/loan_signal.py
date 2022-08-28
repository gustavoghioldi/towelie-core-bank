import logging
from loans.models.loan import Loan, LoanCycleLifeStatus
from loans.models.loan_ledger import LoanLedger
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from dateutil.relativedelta import *
from loans.services.payments_calculator_service import PaymentsCalculatorService
from django.core.exceptions import ValidationError
from loans.helpers.loan_calculate_helper import LoanCalculateHelper

logger = logging.getLogger(__name__)

@receiver(pre_save, sender=Loan)
def loan_receiver_pre_save(sender, instance:Loan, **kwargs):
    pass

@receiver(post_save, sender=Loan)
def loan_receiver_post_save(sender, instance: Loan, created, **kwargs):
    logging.info(f'post_save {instance}')
    if created:
        _create_loan_ledger(instance)
        if instance.status != LoanCycleLifeStatus.SUBMITTED:
            raise ValidationError(f'SUBMITTED is only accepted as status when creating a new loan')

def _create_loan_ledger(instance: Loan)->None:
    payments = list(range(1, instance.number_of_repayments+1))
    next_repayment = instance.first_repayment_on
    lch = LoanCalculateHelper(instance.principal, instance.number_of_repayments, instance.nominal_interes_rate)
    for i in payments:
        LoanLedger.objects.create(
            loan=instance,
            payment=i,
            payment_date = next_repayment,
            payment_amount = lch.get_payment_detail().get('payment_value')
        )
        next_repayment += relativedelta(months=1)