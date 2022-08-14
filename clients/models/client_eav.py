from django.db import models
from master.models.abstract_model import AbstractModel
from clients.models.client import Client

class ClientEAV(AbstractModel):
    entity = models.ForeignKey(Client, on_delete=models.CASCADE)
    attribute = models.CharField(max_length=25)
    value     = models.CharField(max_length=124)