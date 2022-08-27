from django.contrib.auth import get_user_model
from clients.models.client import Client
from loans.models.loan_purpose import LoanPurpose
from org.models.loan import LoanProduct
from master.models.country import Country
from master.models.currency import Currency

def create_users_and_clients(n_clients: int):
    u = get_user_model()
    for i in list(range(0, n_clients)):
        Client.objects.create(user=u.objects.create_user(username=f'user{i}@mail.com', password=f'user{i}'))

def create_loan_propouse():
    LoanPurpose.objects.create(
        name="varios",
        code="VAR"
    )

def create_countries():
    Country.objects.create(
        name = "Argentina", 
        iso_code = "AR"
    )

def create_currencies():
    Currency.objects.create(
        name = "Pesos Argentinos", 
        iso_code = "ARS"
    )
