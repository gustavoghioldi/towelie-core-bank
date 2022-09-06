import logging
from rest_framework.views import APIView
from rest_framework import status
from master.enums.general import (
    AmortizationType, 
    InteresCalculationPeriod,
    DayInMonth, 
    DayInYears,
    InteresMethod,
    InterestRate
    )
from django.http import HttpResponse
import json
logger = logging.getLogger(__name__)

class OptionListView(APIView):
    def get(self, request, feature,  format=None):
        
        if feature == 'amortization_type':
            feature_class = AmortizationType
        elif feature == 'interes_calculation_period':
            feature_class = InteresCalculationPeriod
        elif feature == 'day_in_month':
            feature_class = DayInMonth
        elif feature == 'day_in_years':
            feature_class = DayInYears
        elif feature == 'interes_method':
            feature_class = InteresMethod
        elif feature == 'interest_rate':
            feature_class = InterestRate      
        else:
            return HttpResponse('',content_type="application/json", status=status.HTTP_404_NOT_FOUND)
        at = list()
        for i in feature_class:
            at.append(i.value)
        return HttpResponse(json.dumps(at),content_type="application/json", status=status.HTTP_200_OK)