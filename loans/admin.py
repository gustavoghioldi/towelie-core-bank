from django.contrib import admin
from loans.models.loan_approved import LoanApproved
from loans.models.loan_disbursement import LoanDisbursement
from loans.models.loan_purpose import LoanPurpose
from loans.models.loan_submitted import LoanSubmitted
from loans.models.loan_ledger import LoanLedger
from loans.models.loan import Loan

@admin.register(LoanLedger)
class LoanLedgerAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'loan', 'payment', 'payment_date', 'payment_amount', 'paid_out', )
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    pass

@admin.register(LoanPurpose)
class LoanPruposeAdmin(admin.ModelAdmin):
    pass

@admin.register(LoanApproved)
class LoanApprovedAdmin(admin.ModelAdmin):
    pass

@admin.register(LoanDisbursement)
class LoanDisbursementAdmin(admin.ModelAdmin):
    pass

@admin.register(LoanSubmitted)
class LoanSubmittedAdmin(admin.ModelAdmin):
    pass