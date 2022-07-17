from django.apps import AppConfig


class FundsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'funds'

    def ready(self):
        from funds.models import fund
        return super().ready()
