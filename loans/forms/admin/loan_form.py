from django import forms
from django.core.exceptions import ValidationError
from loans.models.loan import LoanCycleLifeStatus
class LoanForm(forms.ModelForm):

    def clean(self):
        pass