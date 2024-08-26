import calendar
from dataclasses import dataclass
from datetime import date, datetime

from src.config import (
    MAX_AMOUNT,
    MAX_PERIODS,
    MAX_RATE,
    MIN_AMOUNT,
    MIN_PERIODS,
    MIN_RATE,
)

TOTAL_MONTHS = 12

def add_months(base_date: datetime, months: int) -> date:
    month = base_date.month - 1 + months
    year = base_date.year + month // TOTAL_MONTHS
    month = month % TOTAL_MONTHS + 1
    day = calendar.monthrange(year, month)
    return date(year, month, day[1])


def calculate_deposit(deposit: 'Deposit') -> dict[str, float]:
    rate = deposit.rate / (100 * TOTAL_MONTHS)
    _cur_amount = deposit.amount + rate * deposit.amount
    _cur_date = datetime.strptime(deposit.date, "%d.%m.%Y")
    result = {_cur_date.strftime("%d.%m.%Y"): round(_cur_amount, 2)}
    for _ in range(1, deposit.periods):
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
        """
        Проверка корректности записи количества месяцев при рассчёте депозита.
        """
        return (
                isinstance(self.periods, int) and MIN_PERIODS <= self.periods <= MAX_PERIODS
        )

    def validate_amount(self) -> bool:
        """
        Проверка корректности записи суммы депозита.
        """
        return isinstance(self.amount, int) and MIN_AMOUNT <= self.amount <= MAX_AMOUNT

    def validate_rate(self) -> bool:
        """
        Проверка корректности записи даты.
        """
        return isinstance(self.rate, int) and MIN_RATE <= self.rate <= MAX_RATE

    def validate_date(self) -> bool:
        """
        Проверка корректности записи даты.
        """

        try:
            day, month, year = self.date.split(".")
            if len(day) != 2 or len(month) != 2 or len(year) != 4:
                return False
            datetime.strptime(self.date, "%d.%m.%Y")
            return True
        except ValueError:
            return False

    def validate(self) -> list[str]:
        """
        Проверка корректности полей расчёта депозита.
        """

        attributes = (
            ("DATE", self.validate_date),
            ("PERIODS", self.validate_periods),
            ("AMOUNT", self.validate_amount),
            ("RATE", self.validate_rate),
        )
        result = [item for item, function in attributes if not function()]
        return result
