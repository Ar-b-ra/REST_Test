from unittest import TestCase

from src.deposit_resolver import Deposit, calculate_deposit
from src.config import (
    MAX_AMOUNT,
    MAX_PERIODS,
    MAX_RATE,
    MIN_AMOUNT,
    MIN_PERIODS,
    MIN_RATE,
)


class TestDeposit(TestCase):
    def setUp(self):
        self.test_deposit = Deposit("01.01.2022", 1, 1_0000, 2)

    def test_verify_periods(self):
        self.assertTrue(self.test_deposit.validate_periods())

    def test_verify_periods_negative(self):
        self.test_deposit.periods = MIN_PERIODS - 1
        self.assertFalse(self.test_deposit.validate_periods())
        self.test_deposit.periods = MAX_PERIODS + 1
        self.assertFalse(self.test_deposit.validate_periods())
        self.test_deposit.periods = str(MAX_PERIODS)
        self.assertFalse(self.test_deposit.validate_periods())

    def test_verify_amount(self):
        self.assertTrue(self.test_deposit.validate_amount())

    def test_verify_amount_negative(self):
        self.test_deposit.amount = MIN_AMOUNT - 1
        self.assertFalse(self.test_deposit.validate_amount())
        self.test_deposit.amount = MAX_AMOUNT + 1
        self.assertFalse(self.test_deposit.validate_amount())
        self.test_deposit.amount = str(MAX_AMOUNT)
        self.assertFalse(self.test_deposit.validate_amount())

    def test_verify_rate(self):
        self.assertTrue(self.test_deposit.validate_rate())

    def test_verify_rate_negative(self):
        self.test_deposit.rate = MIN_RATE - 1
        self.assertFalse(self.test_deposit.validate_rate())
        self.test_deposit.rate = MAX_RATE + 1
        self.assertFalse(self.test_deposit.validate_rate())
        self.test_deposit.rate = str(MAX_RATE)
        self.assertFalse(self.test_deposit.validate_rate())

    def test_verify_date(self):
        self.assertTrue(self.test_deposit.validate_date())

    def test_verify_date_negative(self):
        self.test_deposit.date = "32.01.2022"
        self.assertFalse(self.test_deposit.validate_date())
        self.test_deposit.date = "01.01.22"
        self.assertFalse(self.test_deposit.validate_date())
        self.test_deposit.date = "01.1.2022"
        self.assertFalse(self.test_deposit.validate_date())
        self.test_deposit.date = "1.01.2022"
        self.assertFalse(self.test_deposit.validate_date())

    def test_valid_deposit(self):
        deposit = Deposit("01.01.2022", 12, 10000, 5)
        self.assertEqual(deposit.validate(), [])

    def test_invalid_date(self):
        deposit = Deposit("invalid_date", 12, 10000, 5)
        self.assertEqual(deposit.validate(), ["DATE"])

    def test_invalid_periods(self):
        deposit = Deposit("01.01.2022", 0, 10000, 5)
        self.assertEqual(deposit.validate(), ["PERIODS"])

    def test_invalid_amount(self):
        deposit = Deposit("01.01.2022", 12, 0, 5)
        self.assertEqual(deposit.validate(), ["AMOUNT"])

    def test_invalid_rate(self):
        deposit = Deposit("01.01.2022", 12, 10000, 0)
        self.assertEqual(deposit.validate(), ["RATE"])

    def test_multiple_invalid_attributes(self):
        deposit = Deposit("invalid_date", 0, 0, 0)
        self.assertEqual(deposit.validate(), ["DATE", "PERIODS", "AMOUNT", "RATE"])

    def test_calc_deposit(self):
        deposit = Deposit("31.01.2021", 7, 10_000, 6)
        result = calculate_deposit(deposit)
        self.assertEqual(
            {
                "31.01.2021": 10_050.00,
                "28.02.2021": 10_100.25,
                "31.03.2021": 10_150.75,
                "30.04.2021": 10_201.51,
                "31.05.2021": 10_252.51,
                "30.06.2021": 10_303.78,
                "31.07.2021": 10_355.29,
            },
            result,
        )
