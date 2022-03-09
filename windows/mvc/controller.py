from windows.mvc.counter_interface import CounterInterface
from windows.mvc.model import Counter
from windows.mvc.view import View


class CounterControl(CounterInterface):
    def __init__(self):
        self.counter = Counter()
        self.view = View(self)

    def btn_increase_clicked(self):
        self.counter.increase()
        value = self.counter.value
        self.view.update_counter_label(value)

    def btn_decrease_clicked(self):
        self.counter.decrease()
        value = self.counter.value
        self.view.update_counter_label(value)


if __name__ == '__main__':
    control = CounterControl()
    control.view.start()
