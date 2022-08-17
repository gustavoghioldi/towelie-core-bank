import logging
from accounts.models import ClientAccountLedger, ClientAccount
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


logger = logging.getLogger(__name__)

@receiver(pre_save, sender=ClientAccountLedger)
def account_ledger_receiver_pre_save(sender, instance, **kwargs):
    pass

       
@receiver(post_save, sender=ClientAccountLedger)
def account_ledger_receiver_post_save(sender, instance, created, **kwargs):
    if created:
        client_account = ClientAccount.objects.get(uuid=instance.client_account_id)
        if instance.account_ledger_change_type == 'CREDIT':
            client_account.balance += client_account.balance + instance.balance
        if instance.account_ledger_change_type == 'DEBIT':
            client_account.balance += client_account.balance - instance.balance 
        client_account.save()     