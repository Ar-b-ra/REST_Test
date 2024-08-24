import calendar
from dataclasses import dataclass
from datetime import date, datetime

MIN_PERIODS = 1
MAX_PERIODS = 60
MIN_AMOUNT = 10_000
MAX_AMOUNT = 3_000_000
MIN_RATE = 1
MAX_RATE = 8


def add_months(sourcedate: datetime, months: int):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = calendar.monthrange(year, month)
    return date(year, month, day[1])


def calculate_deposit(deposit) -> dict[str, float]:
    rate = deposit.rate / (100 * 12)
    _cur_amount = deposit.amount + rate * deposit.amount
    _cur_date = datetime.strptime(deposit.date, "%d.%m.%Y")
    result = {_cur_date.strftime("%d.%m.%Y"): round(_cur_amount, 2)}
    for i in range(1, deposit.periods):
        _cur_amount += _cur_amount * rate
        _cur_date = add_months(_cur_date, 1)
        result[_cur_date.strftime("%d.%m.%Y")] = round(_cur_amount, 2)
    return result


@dataclass
class Deposit:
    date: str
    periods: int
    amount: int
    rate: int

    def validate_periods(self) -> bool:
        return (
            isinstance(self.periods, int) and MIN_PERIODS <= self.periods <= MAX_PERIODS
        )

    def validate_amount(self):
        return isinstance(self.amount, int) and MIN_AMOUNT <= self.amount <= MAX_AMOUNT

    def validate_rate(self):
        return isinstance(self.rate, int) and MIN_RATE <= self.rate <= MAX_RATE

    def validate_date(self):
        try:
            day, month, year = self.date.split(".")
            if len(day) != 2 or len(month) != 2 or len(year) != 4:
                return False
            datetime.strptime(self.date, "%d.%m.%Y")
            return True
        except ValueError:
            return False

    def validate(self):
        attributes = (
            ("DATE", self.validate_date),
            ("PERIODS", self.validate_periods),
            ("AMOUNT", self.validate_amount),
            ("RATE", self.validate_rate),
        )
        result = [item for item, function in attributes if not function()]
        return result
