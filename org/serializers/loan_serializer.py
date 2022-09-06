import logging
from rest_framework import serializers
from org.models.loan import LoanProduct

logger = logging.getLogger(__name__)

class LoanProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanProduct
        fields = '__all__'