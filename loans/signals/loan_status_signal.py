import logging
from loans.models.loan_status import Approved, Disbursed
from loans.models.loan import Loan
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from loans.models.loan import LoanCycleLifeStatus
logger = logging.getLogger(__name__)

@receiver(pre_save, sender=Approved)
def loan_approved_pre_save(sender, instance:Approved, **kwargs):
    if Approved.objects.filter(loan=instance.loan).count() >= 1:
        raise ValidationError(f'loan {instance.loan} have 1 or more approved' )

@receiver(post_save, sender=Approved)
def loan_approved_post_save(sender, instance: Approved, created, **kwargs):
    if created:
        loan = Loan.objects.get(uuid=instance.loan.uuid)
        loan.status = LoanCycleLifeStatus.APPROVED.value
        loan.save()

@receiver(pre_save, sender=Disbursed)
def loan_disbursed_pre_save(sender, instance:Disbursed, **kwargs):
    if Disbursed.objects.filter(loan=instance.loan).count() >= 1:
        raise ValidationError(f'loan {instance.loan} have 1 or more disbursed' )

@receiver(post_save, sender=Disbursed)
def loan_disbursed_post_save(sender, instance: Disbursed, created, **kwargs):
    if created:
        loan = Loan.objects.get(uuid=instance.loan.uuid)
        loan.status = LoanCycleLifeStatus.DISBURSED.value
        loan.save()