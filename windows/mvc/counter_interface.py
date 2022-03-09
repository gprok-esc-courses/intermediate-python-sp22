from abc import abstractmethod


class CounterInterface:
    @abstractmethod
    def btn_increase_clicked(self):
        raise NotImplementedError()

    @abstractmethod
    def btn_decrease_clicked(self):
        raise NotImplementedError()
