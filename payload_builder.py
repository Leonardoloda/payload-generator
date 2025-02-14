from payload import Payload
from builder import Builder

from base64 import b64encode

class PayloadBuilder(Builder):
    payload: Payload

    def __init__(self) -> None:
        self.reset()

    def get_payload(self) -> Payload:
        return self.payload
    
    def set_queue(self, queue: str):
        self.payload.queue = queue
    
    def set_topic(self, topic: str) -> None:
        self.payload.topic = topic

    def set_environment(self, environment: str) -> None:
        self.payload.environment = environment
    
    def set_sample(self, sample: str) -> None:
        sample_bytes = sample.encode("ascii")
        sample_bytes = b64encode(sample_bytes)
        sample_bytes = sample_bytes.decode("ascii")

        self.payload.sample = sample_bytes
    
    def reset(self) -> None:
        self.payload = Payload()