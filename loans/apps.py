from django.apps import AppConfig


class LoansConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'loans'

    def ready(self) -> None:
        from loans.models import loan, loan_purpose
        return super().ready()
