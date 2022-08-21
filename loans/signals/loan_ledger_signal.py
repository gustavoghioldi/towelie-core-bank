import logging
from loans.models.loan_ledger import LoanLedger
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

logger = logging.getLogger(__name__)

@receiver(pre_save, sender=LoanLedger)
def loan_receiver_pre_save(sender, instance:LoanLedger, **kwargs):
    pass

       
@receiver(post_save, sender=LoanLedger)
def loan_receiver_post_save(sender, instance: LoanLedger, created, **kwargs):
    if created:
        pass