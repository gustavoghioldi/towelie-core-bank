from dataclasses import fields
import logging
from rest_framework import serializers
from django.contrib.auth import get_user_model
from clients.models.client import Client
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


class ClientGETSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Client
        fields = ['uuid', 'user', 'activation_date', 'user_details', 'is_active_client', ]

class ClientPATCHSerializer(serializers.Serializer):
    middle_name = serializers.CharField(max_length=128, allow_null=True, allow_blank=True)
    last_name = serializers.CharField(max_length=128)
    first_name = serializers.CharField(max_length=128)

    def update(self, instance, validated_data):
        instance.middle_name = validated_data.get('middle_name', instance.email)
        instance.last_name   = validated_data.get('last_name', instance.content)
        instance.first_name  = validated_data.get('first_name', instance.created)
        return instance
    
    
    
    
class NewClientUpdateSerializer(serializers.Serializer):
    first_name  = serializers.CharField(max_length=128)
    middle_name = serializers.CharField(max_length=128)
    last_name   = serializers.CharField(max_length=128)
    extra_data  = serializers.DictField()