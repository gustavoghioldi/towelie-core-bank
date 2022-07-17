from django.db import models

class Office(models.Model):
    name = models.CharField(max_length=50)
    opening_date = models.DateField()
    