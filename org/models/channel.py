from django.db import models
from master.models.abstract_model import AbstractModel

class Channel(AbstractModel):
    name = models.CharField(max_length=50)
