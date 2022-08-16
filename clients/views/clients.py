import logging
from rest_framework.views import APIView
from clients.models.client import Client
from rest_framework.response import Response
from rest_framework import status
from clients.serializers.client_serializer import ClientGETSerializer, ClientPATCHSerializer
logger = logging.getLogger(__name__)

class ClientView(APIView):
    def get(self, request, format=None):
        clients = Client.objects.all()
        serializer = ClientGETSerializer(clients, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, format=None):
        serializer =  ClientPATCHSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)    