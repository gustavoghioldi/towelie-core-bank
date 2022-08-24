from django.contrib.auth import get_user_model
from clients.models.client import Client

def create_users_and_clients(n_clients: int):
    u = get_user_model()
    for i in list(range(0, n_clients)):
        Client.objects.create(user=u.objects.create_user(username=f'user{i}@mail.com', password=f'user{i}'))

def create_loan_product():
    pass

def create_loan_propouse():
    pass
