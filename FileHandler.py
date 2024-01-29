class FileHandler:
    @staticmethod
    def read_file(file_path: str) -> str:
        with open(file_path, 'r') as file:
            content = file.read()
        return content

    @staticmethod
    def save_file(file_path: str, content: str) -> None:
        with open(file_path, 'w') as file:
            file.write(content)
