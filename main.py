from payload_builder import PayloadBuilder
from orchestrator import Orchestrator

from os import listdir


payload_builder = PayloadBuilder()
orchestrator = Orchestrator(payload_builder)

def list_files_in_folder(folder_path):
    try:
        files = listdir(folder_path)
        for file in files:
            print(file)
    except Exception as e:
        print(f"An error occurred: {e}")

folder_path = './samples'
list_files_in_folder(folder_path)
