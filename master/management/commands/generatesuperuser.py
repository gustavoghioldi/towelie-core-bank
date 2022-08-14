from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from app.settings import FIRST_ADMIN_USERNAME, FIRST_ADMIN_PASSWORD

class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        User.objects.filter().exists() or User.objects.create_superuser(FIRST_ADMIN_USERNAME, 'admin@admin.com', FIRST_ADMIN_PASSWORD)