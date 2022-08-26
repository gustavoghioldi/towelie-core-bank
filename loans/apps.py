from django.apps import AppConfig


class LoansConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'loans'

    def ready(self) -> None:
        from loans.models import loan, loan_purpose, loan_ledger, loan_status
        from loans.signals import loan_ledger_signal, loan_signal, loan_status_signal
        return super().ready()
