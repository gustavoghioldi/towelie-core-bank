from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self) -> None:
        from accounts.signals import move_in_account_ledger, changes_in_account
        return super().ready()
        