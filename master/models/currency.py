from django.db import models
from master.models.abstract_model import AbstractModel


class Currency(AbstractModel):
    name            = models.CharField(max_length=24, unique=True)
    iso_code        = models.CharField(max_length=3, unique=True)
    symbol          = models.CharField(max_length=3, default="$")
    decimal_places  = models.SmallIntegerField(default=2)
    active          = models.BooleanField()

    class Meta:
        verbose_name_plural = "Currencies"

    def __str__(self) -> str:
        return self.iso_code
