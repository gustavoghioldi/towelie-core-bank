import logging
from rest_framework import serializers
from clients.models.client import Client, ClientAddresses, ClientIds
from clients.serializers.aux import ClientCountrySerializer

logger = logging.getLogger(__name__)

class ClientGETSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Client
        fields = ['uuid', 'user', 'activation_date', 'user_details', 'is_active_client', 'country', 'client_ids', 'client_addresses' ]
    
class ClientPATCHSerializer(serializers.Serializer):
    middle_name = serializers.CharField(max_length=128, required=False)
    last_name = serializers.CharField(max_length=128, required=False)
    first_name = serializers.CharField(max_length=128, required=False)
    country = ClientCountrySerializer(required=False)

    def update(self, instance, validated_data):
        instance.middle_name = validated_data.get('middle_name', instance.middle_name)
        instance.user.last_name   = validated_data.get('last_name', instance.user.last_name)
        instance.user.first_name  = validated_data.get('first_name', instance.user.first_name)
        if validated_data.get('country'):
            instance.country_nationality = validated_data.get('country').get('nationality', instance.country_nationality)
            instance.country_residence = validated_data.get('country').get('residence', instance.country_residence)
        instance.user.save()
        instance.save()
        return instance

class ClientAddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientAddresses
        fields = '__all__'

class ClientIdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientIds
        fields = '__all__'