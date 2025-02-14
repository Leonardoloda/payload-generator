from abc import ABC, abstractmethod

class Step(ABC):
    next_step = None

    def __init__(self) -> None:
        pass

    @abstractmethod
    def execute(self, *args):
        pass

    def next(self, next_step) -> None:
        self.next_step = next_step

        return next_step;