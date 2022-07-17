from django.urls import path

from api.views import ClientView

urlpatterns = [
    path('clients', ClientView.as_view(), name='api-clients'),]