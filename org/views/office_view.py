import logging
from rest_framework import generics
from clients.models.client import Client
from rest_framework.response import Response
from org.models.office import Office
from org.serializers.office_serializer import OfficeSerializer
logger = logging.getLogger(__name__)

class OfficeListCreateView(generics.ListCreateAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer

class OfficeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer    