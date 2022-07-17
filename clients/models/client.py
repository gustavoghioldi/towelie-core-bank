from django.db import models

class Client(models.Model):
    first_name        = models.CharField(max_length=100) 
    middle_name       = models.CharField(max_length=100)
    last_name         = models.CharField(max_length=100)
    active            = models.BooleanField(default=False) 
    activation_date   = models.DateField(null=True, blank=True)
