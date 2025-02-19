from abc import ABC, abstractmethod

class Step(ABC):
    next_step = None

    @abstractmethod
    def execute(self, *args):
        pass

    def next(self, next_step) -> None:
        self.next_step = next_step

        return next_step
