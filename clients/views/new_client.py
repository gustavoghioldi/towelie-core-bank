import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from clients.serializers.new_client_serializer import NewClientCreateSerializer, NewClientValidateEmailSerializer
from rest_framework import status
from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__)

class NewClientView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def post(self, request, format=None):
        serializer = NewClientCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = get_user_model()
            user.objects.create_user(
                username=request.data.get("username"), 
                email=request.data.get("username"), 
                password=request.data.get("password"), 
                is_active=False)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        serializer = NewClientValidateEmailSerializer(data=
        {
            "username": request.query_params.get("username"),
            "uuid":request.query_params.get("uuid")
        })
        if serializer.is_valid():
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)