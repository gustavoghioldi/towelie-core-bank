from django.test import TestCase
from app.test_setup.test_set_up_data import (
    create_loan_propouse, 
    create_users_and_clients, 
    create_countries, 
    create_currencies)
from loans.models.loan import Loan
from master.enums.general import AmortizationType, DayInYears, InteresCalculationPeriod, InteresMethod, RepaymenthStrategy, DayInMonth     
from org.models.loan import LoanProduct
from master.models.country import Country
from master.models.currency import Currency
from clients.models.client import Client
from loans.models.loan_purpose import LoanPurpose
from loans.models.loan_ledger import LoanLedger
import datetime

class LoanTestClass(TestCase):

    def setUp(self):
        create_users_and_clients(1)
        create_loan_propouse()
        create_countries()
        create_currencies()
        LoanProduct.objects.create(
            name = "Adelanto de sueldo",
            short_name="ADS",
            description="nada",
            start_date = datetime.date.today(),
            close_date = datetime.date.today(),
            currency = Currency.objects.filter()[0],
            country= Country.objects.filter()[0],
            amount_multiples = 1,
            principal_max = 1000,
            principal_min = 100,
            repayments_max = 1,
            repayments_min = 1,
            repayment_step = 1,
            #fund_origin
            amortization = AmortizationType.EQUALS_INSTALLMENTS.value, 
            nominal_interes_rate = 0.0,
            interes_method = InteresMethod.FLAT.value,
            interes_calculation_period = InteresCalculationPeriod.SAME_AS_REPAYMENT_PERIOD.value, 
            repaymenth_strategy = RepaymenthStrategy.PENALTIES_FEES_INTEREST_PRINCIPAL.value , 
            interest_free_period = 0,
            days_in_years        = DayInYears._365.value,
            day_in_month         = DayInMonth._30.value
        )    
    def tearDown(self):
        pass

    def test_loan_1_payments_0_interest(self):
        client = Client.objects.get(user__username="user0@mail.com")
        client.activation_date = datetime.date.today()
        client.save()
        Loan.objects.create(
            client= Client.objects.get(user__username="user0@mail.com"),
            loan_product = LoanProduct.objects.filter()[0],
            loan_prupose = LoanPurpose.objects.filter()[0],
            principal = 999,
            number_of_repayments = 1,
            first_repayment_on = datetime.date.today()
        )
        loan_ledger = LoanLedger.objects.filter(loan__client=client)
        
        self.assertEquals(loan_ledger.count(), 1)
        self.assertEquals(loan_ledger[0].payment_amount, 999)

    def test_something_that_will_fail(self):
        client = Client.objects.get(user__username="user0@mail.com")
        client.activation_date = datetime.date.today()
        client.save()
        with self.assertRaises(Exception):
            
            Loan.objects.create(
                client= Client.objects.get(user__username="user0@mail.com"),
                loan_product = LoanProduct.objects.filter()[0],
                loan_prupose = LoanPurpose.objects.filter()[0],
                principal = 1,
                number_of_repayments = 1,
                first_repayment_on = datetime.date.today()
            )
        