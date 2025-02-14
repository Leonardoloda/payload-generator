from abc import ABC, abstractmethod

class Builder(ABC):
    @abstractmethod

    def reset(self):
        pass

    @abstractmethod
    def set_queue(self, queue: str) -> None:
        pass

    @abstractmethod
    def set_topic(self, topic: str) -> None:
        pass

    @abstractmethod
    def set_environment(self, environment: str) -> None:
        pass

    @abstractmethod
    def set_sample(self, sample: str) -> None:
        pass