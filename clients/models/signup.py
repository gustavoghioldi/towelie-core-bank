from datetime import datetime, timedelta
import logging

from django.db import models
from django.contrib.auth.models import User
from master.models.abstract_model import AbstractModel
from django.db.models.signals import post_save
from django.dispatch import receiver

logger = logging.getLogger(__name__)
class Signup(AbstractModel):
    user = models.ForeignKey(User, unique=True ,on_delete=models.CASCADE)
    expires_at = models.DateTimeField()

@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    from clients.models.signup import Signup
    if created:
        logger.debug("create_user_signal")
        expires_at = datetime.now() + timedelta(hours = 1)
        Signup.objects.create(user=instance, expires_at=expires_at)
        
