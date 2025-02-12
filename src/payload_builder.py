from payload import Payload
from builder import Builder

class PayloadBuilder(Builder):
    payload: Payload

    def __init__(self) -> None:
        self.reset()

    def get_payload(self) -> Payload:
        return self.payload
    
    def set_application(self, application: str) -> None:
        self.payload.application = application

    def set_environment(self, environment: str) -> None:
        self.payload.environment = environment
    
    def set_sample(self, sample: str) -> None:
        self.payload.sample = sample
    
    def reset(self) -> None:
        self.payload = Payload()