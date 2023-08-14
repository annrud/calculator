from Client import ConsoleView
from Calculator.Calculator import CaloriesCalculator, CashCalculator, Record


class Presenter:

    def __init__(self, view: ConsoleView) -> None:
        self.view = view

    MENU = {
        '1': 'Расчёт калорий',
        '2': 'Расчёт денег',
        '0': 'Выход',
    }
    MENU_CURRENCY = {
        '1': 'RUB',
        '2': 'USD',
        '3': 'EUR',
        '0': 'Выход',
    }
    MENU_CASH = {
        '1': 'Добавить новую запись в список покупок',
        '2': 'Количество потраченных денег сегодня',
        '3': 'Количество потраченных денег за неделю',
        '4': 'Проверить остаток денег',
        '0': 'Выход',
    }
    MENU_KCAL = {
        '1': 'Добавить новую запись в список съеденного',
        '2': 'Количество съеденных ккал на сегодня',
        '3': 'Количество съеденных ккал за неделю',
        '4': 'Проверить сколько ккал можно ещё съесть',
        '0': 'Выход',
    }

    def readme(self) -> None:
        print("""
        Программа "Калькулятор для расчета калорий и денег"
        рассчитывает остаток денег/калорий на сегодня,
        потраченных денег или съеденных калорий за сегодня/за неделю.
        """)

    def get_calc(self) -> None:
        if self.view.get_choice('Выберите калькулятор:', self.MENU) == "1":
            self.choice_kcal()
        else:
            self.choice_cash()

    def choice_kcal(self) -> None:
        kcal = self.view.get_number('Введите количество ккал на день: ')
        kcal_calc = CaloriesCalculator(kcal)
        while True:
            action = self.view.get_choice('Выберите : ', self.MENU_KCAL)
            match action:
                case '1':
                    food = input('Что съели: ')
                    eaten = self.view.get_number('Сколько ккал было в еде: ')
                    record = Record(amount=eaten, comment=food)
                    kcal_calc.add_record(record)
                    print('Спасибо, запись добавлена')
                case '2':
                    print(kcal_calc.get_today_stats())
                case '3':
                    print(kcal_calc.get_week_stats())
                case '4':
                    print(kcal_calc.get_calories_remained())
                case _:
                    break

    def choice_cash(self) -> None:
        currency = self.MENU_CURRENCY[self.view.get_choice(
            'Выберите валюту:', self.MENU_CURRENCY
        )]
        cash = self.view.get_number('Введите количество денег в рублях: ')
        cash_calc = CashCalculator(cash)
        while True:
            action = self.view.get_choice('Выберите : ', self.MENU_CASH)
            match action:
                case '1':
                    purchase = input('Приобретение: ')
                    spent = self.view.get_number(
                        'Введите количество потраченных денег в рублях: '
                    )
                    record = Record(amount=spent, comment=purchase)
                    cash_calc.add_record(record)
                    print('Спасибо, запись добавлена')
                case '2':
                    print(cash_calc.get_today_stats())
                case '3':
                    print(cash_calc.get_week_stats())
                case '4':
                    print(cash_calc.get_today_cash_remained(currency))
                case _:
                    break
