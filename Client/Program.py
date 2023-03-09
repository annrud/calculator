from Client.ConsoleView import View
from Client.Presenter import Presenter

if __name__ == '__main__':

    presenter = Presenter(View())
    presenter.readme()
    presenter.get_calc()
