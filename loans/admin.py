from django.contrib import admin

from loans.models.loan_purpose import LoanPurpose
from loans.models.loan import Loan

# Register your models here.
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    pass

@admin.register(LoanPurpose)
class LoanPruposeAdmin(admin.ModelAdmin):
    pass