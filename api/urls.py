from django.urls import path

from clients.views.new_client import NewClientView
from clients.views.clients import ClientReadView, ClientEditView, ClientAddDeleteView
urlpatterns = [
    path('create_client', NewClientView.as_view(), name='api-new-clients'),
    path('clients', ClientReadView.as_view(), name='api-clients-read'),
    path('clients/<client_id>', ClientEditView.as_view(), name='api-client-edit'),
    path('clients/<feature>/<client_id>', ClientAddDeleteView.as_view(), name='api-client-add-delete-feature'),
    
    ]