from rest_framework import generics
from org.serializers.loan_serializer import LoanProductSerializer
from org.models.loan import LoanProduct

class LoanListCreateView(generics.ListCreateAPIView):
    queryset = LoanProduct.objects.all()
    serializer_class = LoanProductSerializer

class LoanRetrieveView(generics.RetrieveAPIView):
    queryset = LoanProduct.objects.all()
    serializer_class = LoanProductSerializer