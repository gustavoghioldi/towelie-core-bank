import datetime
import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from clients.models.signup import Signup

logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    if created:
        logger.debug("create_user_signal")
        expires_at = datetime.datetime.now() + datetime.timedelta(hours = 1)
        Signup.objects.create(user=instance, expires_at=expires_at)

@receiver(post_save, sender=User)
def user_pre_save(sender, instance, created, **kwargs):
    pass
        