from django.apps import AppConfig


class ClientConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clients'

    def ready(self) -> None:
        from .models import client_account, client_eav, client_meta, signup
        return super().ready()