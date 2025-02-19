from os import listdir

class FileHandler:
    def list_files_in_folder(self, folder_path: str) -> list[str]:
        try:
            return listdir(folder_path)
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def read_file(self, file_path: str) -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            print(f"An error occurred: {e}")
