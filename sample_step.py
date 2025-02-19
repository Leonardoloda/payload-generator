from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt

from step import Step
from files_handler import FileHandler

class SampleStep(Step):
    def __init__(self, console: Console, file_handler: FileHandler) -> None:
        super().__init__()
        self.console = console
        self.file_handler = file_handler

    def execute(self, path: str) -> str:
        samples = self.file_handler.list_files_in_folder(path)

        env_table = Table(title="Available Samples", show_header=True, header_style="bold magenta")
        env_table.add_column("Option", style="cyan")
        env_table.add_column("Sample file", style="yellow")

        for idx, env in enumerate(samples, start=1):
            env_table.add_row(str(idx), env)

        self.console.print(env_table)

        selected_file = Prompt.ask(
            "Please select an environment (by number)",
            choices=[str(i) for i in range(1, len(samples) + 1)]
        )
        selected_filename = samples[int(selected_file) - 1]

        sample = self.file_handler.read_file(f"{path}/{selected_filename}")

        return sample
