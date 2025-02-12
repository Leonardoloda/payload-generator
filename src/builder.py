from abc import ABC, abstractmethod

class Builder(ABC):
    @abstractmethod

    def reset(self):
        pass
    
    @abstractmethod
    def set_application(self, application):
        pass

    @abstractmethod
    def set_environment(self, environment):
        pass

    @abstractmethod
    def set_sample(self, sample):
        pass