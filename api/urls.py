from django.urls import path

from clients.views.new_client import NewClientView
from clients.views.clients import ClientReadView, ClientEditView, ClientAddDeleteView
from org.views.office_view import OfficeRetrieveUpdateDestroyView, OfficeListCreateView
from org.views.loan_view import LoanListCreateView, LoanRetrieveView
from org.views.options_view import OptionListView
from org.views.account_view import AccountListCreateView, AccountRetrieveView
urlpatterns = [
    ### client #####
    path('create_client', NewClientView.as_view(), name='api-new-clients'),
    path('clients', ClientReadView.as_view(), name='api-clients-read'),
    path('clients/<client_id>', ClientEditView.as_view(), name='api-client-edit'),
    path('clients/<feature>/<client_id>', ClientAddDeleteView.as_view(), name='api-client-add-delete-feature'),
    ### org ###
    path('org/office', OfficeListCreateView.as_view(), name='api-org-office'),
    path('org/office/<pk>', OfficeRetrieveUpdateDestroyView.as_view(), name='api-org-office-details'),
    path('org/loan', LoanListCreateView.as_view(), name='api-org-loan'),
    path('org/loan/options/<feature>', OptionListView.as_view(), name='api-org-loan-details'),
    path('org/loan/<pk>', LoanRetrieveView.as_view(), name='api-org-loan-details'),
    path('org/account', AccountListCreateView.as_view(), name='api-org-account'),
    path('org/account/<pk>', AccountRetrieveView.as_view(), name='api-org-account-details'),
    ]