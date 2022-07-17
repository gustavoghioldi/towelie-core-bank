from django.contrib import admin
from org.models.account import AccountProduct
from org.models.channel  import Channel
from org.models.loan import LoanProduct
from org.models.office import Office

@admin.register(AccountProduct)
class AccountProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    pass

@admin.register(LoanProduct)
class LoanProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    pass
