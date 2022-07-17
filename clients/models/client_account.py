from django.db import models
from clients.models.client import Client
from master.models.abstract_model import AbstractModel
from org.models.account import AccountProduct

class ClientAccount(AbstractModel):
    client          = models.ForeignKey(Client, on_delete=models.DO_NOTHING, related_name='clientAccount')
    account_product = models.ForeignKey(AccountProduct, on_delete=models.DO_NOTHING)
    