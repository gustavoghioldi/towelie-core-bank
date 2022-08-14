from master.models.abstract_model import AbstractModel
from django.db import models
from django.contrib.auth.models import User

class Client(AbstractModel):
    user              = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name       = models.CharField(max_length=100)
    activation_date   = models.DateField(null=True, blank=True)



