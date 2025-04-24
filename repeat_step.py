from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from step import Step

class RepeatStep(Step):
    def __init__(self, console: Console):
        self.console = console or Console()


    def execute(self, *args):
        table = Table(title="Reuse Payload Options")

        table.add_column("Option", justify="center", style="cyan", no_wrap=True)
        table.add_column("Description", justify="left", style="magenta")

        table.add_row("1", "Use the current event")
        table.add_row("2", "Create a new event")

        self.console.print(table)

        choice = Prompt.ask("Please select an option", choices=["1", "2"], default="1")

        if choice == "1":
            self.console.print("[green]The payload has been copied to the clipboard.[/green]")
        elif choice == "2":
            self.console.print("[green]You chose to create a new event.[/green]")

        return choice == "1"
