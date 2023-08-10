import collections
import sys


class View:
    """Ввод данных пользователем."""

    def __init__(self) -> None:
        self.calc = None

    def get_choice(self, title, menu) -> str:
        while True:
            try:
                print(title)
                ord_menu = collections.OrderedDict(sorted(menu.items()))
                ord_menu.move_to_end('0')
                self.calc = input('\n'.join(
                    [f'{key}: {value}' for key, value in ord_menu.items()]
                ) + '\n')
                if self.calc not in menu.keys():
                    raise ValueError
                if self.calc == '0':
                    sys.exit()
                return self.calc
            except ValueError:
                print('Неверный ввод!')

    def get_number(self, title) -> float:
        while True:
            number = input(title)
            try:
                if number.isdigit():
                    return int(number)
                else:
                    raise ValueError
            except ValueError:
                print('Неверно введено число!')
