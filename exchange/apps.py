from django.apps import AppConfig


class ExchangeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'exchange'

    def ready(self) -> None:
        from exchange.models import historical_price
        return super().ready()