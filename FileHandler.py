class FileHandler:
    def __init__(self, file_path: str):
        self.file_content: str = ""
        self.file_content_lines: list = []
        self.refactored_file_content: str = ""
        self.input_file_path: str = file_path

        self.read_file()

    def get_file_content(self) -> str:
        return self.file_content
    
    def get_file_content_lines(self) -> list:
        return self.file_content_lines

    def read_file(self) -> None:
        with open(self.input_file_path, 'r') as file:
            self.file_content = file.read()
            self.file_content_lines = self.file_content.splitlines()

    def refactor_file(self, imports_list: list, globals_list: list, classes_list: list, functions_list: list) -> None:
        # Add each line from the parameters into the refactored_file_content
        self.refactored_file_content += '\n'.join(map(str, imports_list)) + '\n'
        self.refactored_file_content += '\n'.join(map(str, globals_list)) + '\n'
        self.refactored_file_content += '\n'.join(map(str, classes_list)) + '\n'
        self.refactored_file_content += '\n'.join('\n'.join(map(str, function)) for function in functions_list) + '\n'

    def save_file(self, new_file_path_name: str) -> None:
        with open(new_file_path_name, 'w') as file:
            file.write(self.refactored_file_content)


if __name__ == "__main__":
    file_handler = FileHandler("test_file.py")
    file_handler.read_file()
