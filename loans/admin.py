from django.contrib import admin
from loans.models.loan_purpose import LoanPurpose
from loans.models.loan_ledger import LoanLedger
from loans.models.loan import Loan
from loans.models.loan_status import Approved, Disbursed
from django.urls import reverse
from django.utils.html import format_html
from loans.forms.admin.loan_form import LoanForm

@admin.register(LoanLedger)
class LoanLedgerAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'loan', 'payment', 'payment_date', 'payment_amount', 'paid_out', )

class DisbursedAdmin(admin.StackedInline):
    model = Disbursed
    extra = 0
    readonly_fields = ('user',)

    def save_formset(self, request, form, formset, change):
        #instances = formsets[0].save(commit=False)
        pass

class ApprovedAdmin(admin.StackedInline):
    model = Approved
    extra = 0
    readonly_fields = ('user',)
    

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    form = LoanForm
    list_display = ('uuid', 'client', 'loan_product', 'principal', 'number_of_repayments', 'status', )
    readonly_fields = ('uuid', 'subimtted_by', 'status', )
    list_filter = ('client', 'loan_product', 'status', )
    inlines = [ApprovedAdmin, DisbursedAdmin]

    def save_related(self, request, form, formsets, change):
        instances = [f.save(commit=False) for f in formsets]
        for i in instances:
            if len(i) == 1:
                j = i[0]
                j.user = request.user
        super(LoanAdmin, self).save_related(request, form, formsets, change)        
    
    def save_model(self, request, obj, form, change):
        if not obj.subimtted_by:
            obj.subimtted_by = request.user
            obj.save()
        
    # def cycle_life_url(self, obj):
    #     url = reverse('admin:%s_%s_change' % (obj.cycle._meta.app_label,  obj.cycle._meta.model_name),  args=[obj.cycle.pk] )
    #     return format_html(f'<a href="{url}">{obj.cycle.status} </a>')

# /admin/loans/loancyclelife/0e4567b9-37e6-4c0c-b306-009a2ba4ac6f/change/
@admin.register(LoanPurpose)
class LoanPruposeAdmin(admin.ModelAdmin):
    pass

@admin.register(Approved)
class ApprovedAdminAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

@admin.register(Disbursed)
class DisbursedAdminAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()