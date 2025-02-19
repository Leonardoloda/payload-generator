from rich.console import Console

from payload_builder import PayloadBuilder
from files_handler import FileHandler

from welcome_step import WelcomeStep
from application_step import ApplicationStep
from sample_step import SampleStep
from environment_step import EnvironmentStep
from result_step import ResultStep

from config import APPLICATION_CHOICES, ENVIRONMENT_CHOICES, APPLICATION_CONFIG, PATHS_CONFIG

console = Console()

payload_builder = PayloadBuilder()
file_handler = FileHandler()

welcome = WelcomeStep(console)
app_selection = ApplicationStep(console, APPLICATION_CHOICES)
env_selection = EnvironmentStep(console, ENVIRONMENT_CHOICES)
sample_selection = SampleStep(console, file_handler)
result = ResultStep(console)

while True:
    welcome.execute()
    welcome.next(app_selection)

    target_app = app_selection.execute()
    app_selection.next(sample_selection)

    sample = sample_selection.execute(path=PATHS_CONFIG[target_app])
    sample_selection.next(env_selection)

    target_env = env_selection.execute()

    queue = APPLICATION_CONFIG[target_app].get("QUEUE_NAME")
    topic = APPLICATION_CONFIG[target_app].get("TOPIC")

    payload_builder.set_queue(queue)
    payload_builder.set_topic(topic)
    payload_builder.set_environment(target_env)
    payload_builder.set_sample(sample)

    created_payload = payload_builder.get_payload()
    created_payload.copy()

    console.clear()

    env_selection.next(result)
    result.execute(created_payload.print())
