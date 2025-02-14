from rich.panel import Panel
from step import Step

class WelcomeStep(Step):
    def __init__(self, console) -> None:
        self.console = console

    def execute(self) -> None:
        panel = Panel.fit(
            "Welcome to the Payload Builder",
            style="bold green",
        )

        self.console.print(panel)