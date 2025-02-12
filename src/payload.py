from pyperclip import copy

class Payload:
    environment: str
    application: str
    sample: str

    def __init__(self):
        self.environment = ""
        self.application = ""
        self.sample = ""

    def copy(self):
        copy({
            "eventSource":"aws:kafka",
            "eventSourceArn":"arn:aws:kafka:us-east-1:123456789012:cluster/vpc-2priv-2pub/751d2973-a626-431c-9d4e-d7975eb44dd7-2",
            "bootstrapServers":"b-2.demo-cluster-1.a1bcde.c1.kafka.us-east-1.amazonaws.com:9092,b-1.demo-cluster-1.a1bcde.c1.kafka.us-east-1.amazonaws.com:9092",
            "records":{
                f"{self.environment}":[
                    {
                        "topic": f"{self.environment}",
                        "partition":0,
                        "offset":15,
                        "timestamp":1545084650987,
                        "timestampType":"CREATE_TIME",
                        "key":"abcDEFghiJKLmnoPQRstuVWXyz1234==",
                        "value":"SGVsbG8sIHRoaXMgaXMgYSB0ZXN0Lg==",
                        "headers": []
                    }
                ]
            }
        })

    def __str__(self):
        return f"Payload: {self.application} - {self.environment} - {self.sample}"