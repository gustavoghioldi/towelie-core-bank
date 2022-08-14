from django.urls import path

from clients.views.new_client import NewClientView
urlpatterns = [
    path('create_client', NewClientView.as_view(), name='api-new-clients'),]