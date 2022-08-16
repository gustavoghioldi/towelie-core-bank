from master.models.abstract_model import AbstractModel
from django.db import models
from django.contrib.auth.models import User

class Client(AbstractModel):
    user              = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name       = models.CharField(max_length=100)
    activation_date   = models.DateField(null=True, blank=True)

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
    def is_active_client(self):
        return True if self.activation_date else False
    

