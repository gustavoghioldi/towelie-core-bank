from django.db import models
from master.models.abstract_model import AbstractModel


class Exchange(AbstractModel):
    code = models.CharField(max_length=255, blank=False, null=False, unique=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    base_url = models.CharField(max_length=255, blank=False, null=False)
