from rich.panel import Panel
from rich.console import Console
from rich.json import JSON

from step import Step

class ResultStep(Step):
    def __init__(self, console: Console) -> None:
        self.console = console

    def execute(self, payload: dict) -> None:
        self.console.print(Panel.fit("Payload Generated:", title="Payload", style="bold blue"))
        self.console.print(JSON.from_data(payload))