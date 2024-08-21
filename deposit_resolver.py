from dataclasses import dataclass
from datetime import datetime

MIN_PERIODS = 1
MAX_PERIODS = 60
MIN_AMOUNT = 10_000
MAX_AMOUNT = 3_000_000
MIN_RATE = 1
MAX_RATE = 8


@dataclass
class Deposit:
    date: str
    periods: int
    amount: int
    rate: int

    def verify_periods(self) -> bool:
        return (
            isinstance(self.periods, int) and MIN_PERIODS <= self.periods <= MAX_PERIODS
        )

    def verify_amount(self):
        return isinstance(self.amount, int) and MIN_AMOUNT <= self.amount <= MAX_AMOUNT

    def verify_rate(self):
        return isinstance(self.rate, int) and MIN_RATE <= self.rate <= MAX_RATE

    def verify_date(self):
        day, month, year = self.date.split(".")
        if len(day) != 2 or len(month) != 2 or len(year) != 4:
            return False
        try:
            datetime.strptime(self.date, "%d.%m.%Y")
            return True
        except ValueError:
            return False
