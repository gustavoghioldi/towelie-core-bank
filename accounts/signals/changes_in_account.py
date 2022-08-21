import logging
from accounts.models import ClientAccount
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


logger = logging.getLogger(__name__)

@receiver(pre_save, sender=ClientAccount)
def account_ledger_receiver_pre_save(sender, instance, **kwargs):
    pass

       
@receiver(post_save, sender=ClientAccount)
def account_ledger_receiver_post_save(sender, instance: ClientAccount, created, **kwargs):
    if instance.default_collector:
        _default_collector(instance)


def _default_collector(instance):
    if ClientAccount.objects.filter(client=instance.client, default_collector=True).count() > 1:
        for i in ClientAccount.objects.filter(client=instance.client, default_collector=True):
            if i.uuid != instance.uuid:
                i.default_collector = False
                i.save()
                