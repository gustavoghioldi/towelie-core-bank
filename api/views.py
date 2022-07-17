from rest_framework.generics import ListCreateAPIView
from clients.models.client import Client
from api.serializers.client_serializer import ClientSerializer
# Create your views here.

class ClientView(ListCreateAPIView):
        serializer_class = ClientSerializer
        queryset = Client.objects.all()
        