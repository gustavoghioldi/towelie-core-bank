import logging
from rest_framework import serializers
from org.models.office import Office

logger = logging.getLogger(__name__)

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'