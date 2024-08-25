import unittest
from app import app


class TestDepositRoute(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_valid_deposit(self):
        deposit_json = {"date": "01.01.2022", "periods": 1, "amount": 1_0000, "rate": 2}
        response = self.app.get(
            f"/deposit?date={deposit_json['date']}&periods={deposit_json['periods']}&amount={deposit_json['amount']}&rate={deposit_json['rate']}"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, dict)

    def test_invalid_deposit(self):
        deposit_json = {"date": "32.01.2022", "periods": 1, "amount": 1_0000, "rate": 2}
        response = self.app.get(
            f"/deposit?date={deposit_json['date']}&periods={deposit_json['periods']}&amount={deposit_json['amount']}&rate={deposit_json['rate']}"
        )
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(response.json, dict)
        self.assertIn("error", response.json)

    def test_missing_fields(self):
        deposit_json = {"periods": 1, "amount": 1_0000, "rate": 2}
        response = self.app.get(
            f"/deposit?periods={deposit_json['periods']}&amount={deposit_json['amount']}&rate={deposit_json['rate']}"
        )
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(response.json, dict)
        self.assertIn("error", response.json)

    def test_all_nonefields(self):
        deposit_json = {"date": None, "periods": None, "amount": None, "rate": None}
        response = self.app.get(
            f"/deposit?date={deposit_json['date']}&periods={deposit_json['periods']}&amount={deposit_json['amount']}&rate={deposit_json['rate']}"
        )

        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(response.json, dict)
        self.assertIn("error", response.json)


if __name__ == "__main__":
    unittest.main()
