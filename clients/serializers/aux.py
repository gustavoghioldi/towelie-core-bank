from rest_framework import serializers

class ClientCountrySerializer(serializers.Serializer):
    nationality = serializers.CharField(required=False)
    residence = serializers.CharField(required=False)