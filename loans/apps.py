from django.apps import AppConfig


class LoansConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'loans'

    def ready(self) -> None:
        from loans.models import loan, loan_purpose, loan_ledger
        from loans.signals import loan_ledger_signal, loan_signal
        return super().ready()
