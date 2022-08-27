from django.test import TestCase
from django.contrib.auth import get_user_model
from clients.models.client import Client

class ClientTestModel(TestCase):
    def setUp(self):
        pass

    def test_tasks(self):
        # user = get_user_model()
        # user.objects.create_user(
        #         username="user@mail.com", 
        #         email="user@mail.com", 
        #         password="123456", 
        #         is_active=False)       
        self.assertFalse(False)