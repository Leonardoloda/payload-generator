from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt

from step import Step

class EnvironmentStep(Step):
    def __init__(self, console: Console, environments: list[str]) -> None:
        super().__init__()

        self.console = console
        self.environments = environments

    def execute(self) -> str:
        env_table = Table(
            title="Available Environments",
            show_header=True,
            header_style="bold magenta"
        )
        env_table.add_column("Option", style="cyan")
        env_table.add_column("Environment Name", style="yellow")

        for idx, env in enumerate(self.environments, start=1):
            env_table.add_row(str(idx), env)

        self.console.print(env_table)

        selected_env = Prompt.ask(
            "Please select an environment (by number)",
            choices=[str(i) for i in range(1, len(self.environments) + 1)]
        )
        selected_env_name = self.environments[int(selected_env) - 1]

        return selected_env_name
