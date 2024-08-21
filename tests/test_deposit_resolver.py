from unittest import TestCase

from deposit_resolver import Deposit, MAX_AMOUNT, MAX_PERIODS, MAX_RATE, MIN_AMOUNT, MIN_RATE


class TestDeposit(TestCase):
    def setUp(self):
        self.test_deposit = Deposit("01.01.2022", 1, 1_0000, 2)
    def test_verify_periods(self):
        self.assertTrue(self.test_deposit.verify_periods())

    def test_verify_periods_negative(self):
        self.test_deposit.periods = MIN_AMOUNT - 1
        self.assertFalse(self.test_deposit.verify_periods())
        self.test_deposit.periods = MAX_AMOUNT + 1
        self.assertFalse(self.test_deposit.verify_periods())
        self.test_deposit.periods = str(MAX_AMOUNT)
        self.assertFalse(self.test_deposit.verify_periods())

    def test_verify_amount(self):
        self.assertTrue(self.test_deposit.verify_amount())

    def test_verify_amount_negative(self):
        self.test_deposit.amount = MIN_AMOUNT - 1
        self.assertFalse(self.test_deposit.verify_amount())
        self.test_deposit.amount = MAX_AMOUNT + 1
        self.assertFalse(self.test_deposit.verify_amount())
        self.test_deposit.amount = str(MAX_AMOUNT)
        self.assertFalse(self.test_deposit.verify_amount())

    def test_verify_rate(self):
        self.assertTrue(self.test_deposit.verify_rate())

    def test_verify_rate_negative(self):
        self.test_deposit.rate = MIN_RATE - 1
        self.assertFalse(self.test_deposit.verify_rate())
        self.test_deposit.rate = MAX_RATE + 1
        self.assertFalse(self.test_deposit.verify_rate())
        self.test_deposit.rate = str(MAX_RATE)
        self.assertFalse(self.test_deposit.verify_rate())

    def test_verify_date(self):
        self.assertTrue(self.test_deposit.verify_date())

    def test_verify_date_negative(self):
        self.test_deposit.date = "32.01.2022"
        self.assertFalse(self.test_deposit.verify_date())
        self.test_deposit.date = "01.01.22"
        self.assertFalse(self.test_deposit.verify_date())
        self.test_deposit.date = "01.1.2022"
        self.assertFalse(self.test_deposit.verify_date())
        self.test_deposit.date = "1.01.2022"
        self.assertFalse(self.test_deposit.verify_date())