from pyperclip import copy

class Payload:
    environment: str
    topic: str
    queue: str
    sample: str

    def __init__(self):
        self.environment = ""
        self.topic = ""
        self.queue = ""
        self.sample = ""

    def copy(self) -> None:
        copy(self.print())

    def get_queue(self) -> str:
        return self.queue % self.environment

    def get_topic(self) -> str:
        return self.topic % self.environment

    def print(self) -> dict:
        return {
            "eventSource":"aws:kafka",
            "eventSourceArn":"arn:aws:kafka:us-east-1:123456789012:cluster/vpc-2priv-2pub/751d2973-a626-431c-9d4e-d7975eb44dd7-2",
            # spell-checker: disable-next-line
            "bootstrapServers":"b-2.demo-cluster-1.a1bcde.c1.kafka.us-east-1.amazonaws.com:9092,b-1.demo-cluster-1.a1bcde.c1.kafka.us-east-1.amazonaws.com:9092",
            "records":{
                f"{self.get_queue()}":[
                    {
                        "topic": f"{self.get_topic()}",
                        "partition":0,
                        "offset":15,
                        "timestamp":1545084650987,
                        "timestampType":"CREATE_TIME",
                        "key":"abcDEFghiJKLmnoPQRstuVWXyz1234==",
                        "value": self.sample,
                        "headers": []
                    }
                ]
            }
        }
