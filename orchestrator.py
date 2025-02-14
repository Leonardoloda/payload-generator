from payload_builder import PayloadBuilder

class Orchestrator:
    def __init__(self, builder: PayloadBuilder) -> None:
        self.builder = builder
    
    def build_crew_payload(self) -> None:
        self.builder.set_application("Crew")
        self.builder.set_environment("Production")
        self.builder.set_sample("Sample")

    def build_hotel_payload(self) -> None:
        self.builder.set_application("Hotel")
        self.builder.set_environment("Production")
        self.builder.set_sample("Sample")

    def build_monthly_payload(self) -> None:
        self.builder.set_application("Airline")
        self.builder.set_environment("Production")
        self.builder.set_sample("Sample")