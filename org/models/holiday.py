from django.db import models

class Holiday(AbstractModel):
    name = models.CharField(max_length=50)
    date = models.DateField()
    
