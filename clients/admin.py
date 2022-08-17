from django.contrib import admin

from clients.models.client import Client, ClientIds, ClientAddresses
from clients.models.client_eav import ClientEAV
from clients.models.signup import Signup

### Client
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_user_username', 'client_user_name', 'is_active_client')
    
    @admin.display(description='Client')
    def client_user_username(self, obj):
        return obj.user.username
        
    @admin.display(description='Name')
    def client_user_name(self, obj):
        return f'{obj.user.first_name} {obj.middle_name} {obj.user.last_name}' 

    @admin.display(description='Active Client')
    def is_active_client(self, obj):
        return True if obj.activation_date else False

## ClientEAV
@admin.register(ClientEAV)
class ClientEAVAdmin(admin.ModelAdmin):
    list_display = ('client_user_username', 'attribute', 'value')
    list_filter = ('entity','attribute', 'value')

    @admin.display(description='Client')
    def client_user_username(self, obj):
        return obj.entity.user.username

### SIGNUP
@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    pass

### IDS
@admin.register(ClientIds)
class ClientIdsAdmin(admin.ModelAdmin):
    pass


### Addresses
@admin.register(ClientAddresses)
class ClientAddressesAdmin(admin.ModelAdmin):
    pass

