from django.db import models

class Holiday(models.Model):
    name = models.CharField(max_length=50)
    
