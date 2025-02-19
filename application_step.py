from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

from step import Step

class ApplicationStep(Step):
    def __init__(self, console: Console, apps: list[str]) -> None:
        self.console = console
        self.apps = apps

    def execute(self):
        app_table = Table(
            title="Available Applications",
            show_header=True,
            header_style="bold magenta"
        )

        app_table.add_column("Option", style="cyan")
        app_table.add_column("Application Name", style="yellow")

        for idx, app in enumerate(self.apps, start=1):
            app_table.add_row(str(idx), app)

        self.console.print(app_table)

        selected_app = Prompt.ask(
            "Please select an application (by number)", 
            choices=[str(i) for i in range(1, len(self.apps) + 1)]
        )
        selected_app_name = self.apps[int(selected_app) - 1]

        return selected_app_name
