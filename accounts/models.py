from django.db import models
from clients.models.client import Client

class ClientAccount(models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)

# class FundAccount(models.Model):
    # client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    