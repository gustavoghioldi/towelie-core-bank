import logging
import datetime
from rest_framework import serializers
from django.contrib.auth import get_user_model
from clients.models.signup import Signup

logger = logging.getLogger(__name__)

class NewClientCreateSerializer(serializers.Serializer):
    username = serializers.EmailField()
    password = serializers.CharField(max_length=128)

    def validate_username(self, value):
        user = get_user_model()
        if bool(user.objects.filter(username=value).count()):
            raise serializers.ValidationError("username exists")

    def validate_password(self, value):
        pass

class NewClientValidateEmailSerializer(serializers.Serializer):
    uuid     = serializers.UUIDField()
    username = serializers.EmailField()

    def validate_uuid(self, value):
        signup = Signup.objects.filter(uuid=value) 
        if signup.count() != 1:
            raise serializers.ValidationError("Error uuid")
        elif signup[0].expires_at.replace(tzinfo=None) < (datetime.datetime.now()).replace(tzinfo=None):
            raise serializers.ValidationError("expired uuid")

    def validate_username(self, value):
        User = get_user_model()
        user = User.objects.filter(username=value)
        if user.count() != 1:
            raise serializers.ValidationError("Error username")
        else:
            self._signup_user = user[0]

    def validate(self, data):
        if Signup.objects.filter(
            uuid=self._kwargs.get("data").get("uuid"), 
            user = self._signup_user
            ).count() != 1:
            raise serializers.ValidationError("Error uuid not match email")    
        return data
    
            
