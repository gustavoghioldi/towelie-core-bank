import logging
from rest_framework.views import APIView
from clients.models.client import Client
from rest_framework.response import Response
from rest_framework import status
from clients.serializers.client_serializer import ClientAddressesSerializer, ClientGETSerializer, ClientPATCHSerializer, ClientIdsSerializer

logger = logging.getLogger(__name__)

class ClientReadView(APIView):
    def get(self, request, format=None):
        clients = Client.objects.all()
        serializer = ClientGETSerializer(clients, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ClientEditView(APIView):
    def patch(self, request, client_id, format=None):
        serializer =  ClientPATCHSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(Client.objects.get(uuid=client_id), serializer.data)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)  
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)

class ClientAddDeleteView(APIView):
    '''fetures Ids / adresses'''
    def post(self, request, feature, client_id, format=None):
        request.data['client'] = client_id
        if feature == 'ADDRESS':
            serializer =  ClientAddressesSerializer(data=request.data)
        elif feature == 'ID':
            serializer = ClientIdsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)  
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, feature,  client_id, feature_id, format=None):
        pass