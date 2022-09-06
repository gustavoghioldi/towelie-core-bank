from rest_framework import generics
from org.serializers.account_serializer import AccountProductSerializer
from org.models.account import AccountProduct


class AccountListCreateView(generics.ListCreateAPIView):
    queryset = AccountProduct.objects.all()
    serializer_class = AccountProductSerializer

class AccountRetrieveView(generics.RetrieveAPIView):
    queryset = AccountProduct.objects.all()
    serializer_class = AccountProductSerializer