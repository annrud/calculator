import datetime as dt
from abc import abstractmethod
from typing import List, Optional


DATE_FORMAT = '%d.%m.%Y'


class Record:
    def __init__(self, amount: float,
                 date: Optional[str] = None,
                 comment: str = '') -> None:
        self.amount = amount
        self.date = (dt.date.today() if date is None
                     else dt.datetime.strptime(date, DATE_FORMAT).date())
        self.comment = comment

    def __str__(self):
        return f'{self.comment} - {self.amount} - {self.date}'


class InterfaceCalculator:

    @abstractmethod
    def add_record(self, rec: Record) -> None:
        pass

    @abstractmethod
    def get_balance(self) -> float:
        pass


class Calculator(InterfaceCalculator):

    def __init__(self, limit: float) -> None:
        self.limit = limit
        self.records: List[Record] = []

    def add_record(self, rec: Record) -> None:
        """Добавляет новую запись в список."""
        self.records.append(rec)

    def get_today_stats(self) -> float:
        """Метод возвращает сумму денег/калорий, употребленных за сегодня."""
        today = dt.date.today()
        return sum(rec.amount for rec in self.records
                   if rec.date == today)

    def get_week_stats(self) -> float:
        """Метод возвращает сумму денег/калорий за последние 7 дней."""
        today = dt.date.today()
        day_last_week = today - dt.timedelta(weeks=1)
        return sum(rec.amount for rec in self.records
                   if today >= rec.date > day_last_week)

    def get_balance(self) -> float:
        """Расчёт остатка денег/калорий на сегодня."""
        return self.limit - self.get_today_stats()

    def __str__(self):
        return ';'.join(map(str, self.records))


class CashCalculator(Calculator):

    RUB_RATE = 1
    USD_RATE = 73.76
    EUR_RATE = 87.85

    def get_today_cash_remained(self, currency: str) -> str:
        """Возвращает сообщение об остатке денег на сегодня."""
        currencies = {
            'RUB': (self.RUB_RATE, 'руб'),
            'USD': (self.USD_RATE, 'USD'),
            'EUR': (self.EUR_RATE, 'Euro'),
        }
        if currency not in currencies:
            return f'Неподдерживаемая валюта {currency}'
        balance = self.get_balance()
        if balance == 0:
            return 'Денег нет, держись'
        (rate, currency_name) = currencies[currency]
        currency_balance = round(balance / rate, 2)
        if balance > 0:
            return f'На сегодня осталось {currency_balance} {currency_name}'
        currency_balance = abs(currency_balance)
        return ('Денег нет, держись: '
                f'твой долг - {currency_balance} {currency_name}')


class CaloriesCalculator(Calculator):

    def get_calories_remained(self) -> str:
        """Возвращает сообщение об употреблении калорий на сегодня."""
        balance = self.get_balance()
        if balance <= 0:
            return 'Хватит есть!'
        return ('Сегодня можно съесть что-нибудь ещё, '
                'но с общей калорийностью не более '
                f'{balance} кКал')
