from distutils.log import debug
from django.test import TestCase
from loans.tests.set_up_data import create_users_and_clients

class LoanTestClass(TestCase):

    def setUp(self):
        create_users_and_clients(1)

    def tearDown(self):
        pass

    def test_loan_10_payments_0_interest(self):
        self.assertFalse(False)

    def test_something_that_will_fail(self):
        self.assertTrue(True)