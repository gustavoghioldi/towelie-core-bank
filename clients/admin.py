from django.contrib import admin
from clients.models.client_account import ClientAccount

from clients.models.client import Client
from clients.models.signup import Signup

# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(ClientAccount)
class ClientAccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    pass

