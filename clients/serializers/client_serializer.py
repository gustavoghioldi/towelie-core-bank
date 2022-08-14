import logging
from rest_framework import serializers
from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__)

class NewClientUpdateSerializer(serializers.Serializer):
        first_name  = serializers.CharField(max_length=128)
        middle_name = serializers.CharField(max_length=128)
        last_name   = serializers.CharField(max_length=128)
        extra_data  = serializers.DictField()