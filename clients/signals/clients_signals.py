import datetime
import logging
from clients.models.client import Client
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from clients.models.client_eav import ClientEAV
from clients.models.signup import Signup

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Client)
def client_post_save(sender, instance, created, **kwargs):
    if created:
        #user to active TODO: signal when create ClientEAV
        instance.user.is_active = True
        instance.user.save()
        
        #create EAV
        ClientEAV.objects.create(
                entity=instance,
                attribute='CREATE',
                value=1
            )

        #delete Signup TODO: signal when create ClientEAV
        Signup.objects.get(user=instance.user).delete()    
            
        