from django.test import TestCase
from loans.tests.set_up_data import create_users_and_clients
from loans.helpers.loan_calculate_helper import LoanCalculateHelper
class LoanCalculateHelperTestClass(TestCase):

    def setUp(self):
        create_users_and_clients(1)

    def tearDown(self):
        pass

    def test_basic_loan(self):
        principal = 90000
        payments  = 3
        tea       = 169.4
        
        lch = LoanCalculateHelper(90000, 3, 169.4)
        loan_detail = lch.get_payment_detail()

        self.assertEquals(loan_detail['tem'],8.61)
        self.assertEquals(loan_detail['payment_value'],35307.53)
        self.assertEquals(loan_detail['payment_interest'],15922.60)
        self.assertEquals(loan_detail['loan_total'],105922.60)
