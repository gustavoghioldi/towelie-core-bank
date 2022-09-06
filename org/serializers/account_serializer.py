import logging
from rest_framework import serializers
from org.models.account import AccountProduct

logger = logging.getLogger(__name__)

class AccountProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountProduct
        fields = '__all__'