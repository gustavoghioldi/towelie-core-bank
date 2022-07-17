from django.contrib import admin
from clients.models.client_account import ClientAccount

from clients.models.client import Client
# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(ClientAccount)
class ClientAccountAdmin(admin.ModelAdmin):
    pass

