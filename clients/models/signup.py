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


        
