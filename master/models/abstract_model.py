import uuid
from django.db import models

decimal_field = models.DecimalField(max_digits=48, decimal_places=16, default=0.0)

class AbstractModel(models.Model):
    uuid        = models.UUIDField(primary_key=True,  default=uuid.uuid4)
    external_id = models.CharField(max_length=128, unique=True, null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True