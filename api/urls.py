from django.urls import path

from clients.views.new_client import NewClientView
from clients.views.clients import ClientView
urlpatterns = [
    path('create_client', NewClientView.as_view(), name='api-new-clients'),
    path('clients', ClientView.as_view(), name='api-clients'),
    ]