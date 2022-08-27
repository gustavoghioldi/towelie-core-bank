from master.models.abstract_model import AbstractModel
from django.db import models
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from master.models.country import Country
from django.core.exceptions import ValidationError

class Client(AbstractModel):
    user              = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name       = models.CharField(max_length=100, blank=True, null=True)
    activation_date   = models.DateField(null=True, blank=True)
    country_nationality = models.ForeignKey(Country, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='country_nationality')
    country_residence = models.ForeignKey(Country, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='country_residence')

    def __str__(self):
        return self.user.username
        
    @property
    def addresses(self):
        pass

    @property
    def ids(self):
        pass

    @property
    def last_name(self):
        return f'{self.user.last_name}'
    
    @property
    def first_name(self):
        return f'{self.user.first_name}'
     
    @property
    def user_details(self):
        return {
            'username': self.user.username,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'middle_name': self.middle_name,
        }
    @property
    def country(self):
        return {
            "nationality": self.country_nationality,
            "residence": self.country_residence
        }
    @property
    def is_active_client(self):
        return True if self.activation_date else False

    @property
    def client_ids(self):
        return ClientIds.objects.filter(client=self.uuid).values()
    @property
    def client_addresses(self):
        return ClientAddresses.objects.filter(client=self.uuid).values()

class ClientAddressType(models.TextChoices):
    HOME        = "HOME"
    BUSINESS    = "BUSINESS"
    BILLING     = "BILLING"
    SHIPPING    = "SHIPPING"
    CONTRACT    = "CONTRACT"
    RECIPIENT   = "RECIPIENT"

class ClientAddresses(AbstractModel):
    client      = models.ForeignKey(Client, on_delete=models.CASCADE)
    type        = models.CharField(choices=ClientAddressType.choices, max_length=16)
    description = models.TextField()
    state       = models.CharField(max_length=16)
    country     = models.ForeignKey(Country,  on_delete=models.DO_NOTHING)
    city        =  models.CharField(max_length=128)
    primary     = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = 'Clients Addresses'

    def clean(self) -> None:
        self._validation_errors()
        return super().clean()

    def _validation_errors(self):
        if self.primary:
            if ClientAddresses.objects.filter(client=self.client).count()  > 0:
                raise ValidationError('Client have primry address')
class ClientIds(AbstractModel):
    client      = models.ForeignKey(Client, on_delete=models.CASCADE)
    type        = models.CharField(max_length=16)
    id          = models.CharField(max_length=32)
    country     = models.ForeignKey(Country,  on_delete=models.DO_NOTHING)    

    class Meta:
        verbose_name_plural = 'Clients IDs'
        unique_together = ('client', 'type', 'country')