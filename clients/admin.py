from django.contrib import admin
from clients.models.client_account import ClientAccount

from clients.models.client import Client
from clients.models.client_eav import ClientEAV
from clients.models.signup import Signup

# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass
@admin.register(ClientEAV)
class ClientEAVAdmin(admin.ModelAdmin):
    list_display = ('client_user_username', 'attribute', 'value')

    @admin.display(description='Client')
    def client_user_username(self, obj):
        return obj.entity.user.username

@admin.register(ClientAccount)
class ClientAccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    pass

