from UtilProvider import UtilProvider
from FileHandler import FileHandler

class KaunPaada:
    def __init__(self):
        self.codestring = ""
        self.utils = UtilProvider()
        self.fh = FileHandler("main.py")
        self.functions_list: list = []

        #print(self.long_method_detector(self.codestring))
        #print(self.long_parameter_list_detector(self.codestring))
        self.function_detector(self.codestring)

    # Might have to refactor this, since it's >15 lines currently
    def function_detector(self, code_blob: str) -> list:
        new_function_flag: bool = False
        current_function: list = []
        for line in self.fh.get_file_content_lines():
            line = line.strip()
            if self.utils.is_import_line(line) or self.utils.is_class_definition_line(line) or self.utils.is_empty_string(line):
                continue
            elif self.utils.is_function_definition_line(line) or self.utils.is_module_or_script_line(line):
                if new_function_flag:
                    self.functions_list.append(current_function)
                    current_function = []
                new_function_flag = True
                current_function.append(line)
            else:
                current_function.append(line)
        if current_function not in self.functions_list:
                self.functions_list.append(current_function)

    def long_method_detector(self, function_code_blob: str) -> bool:
        # Detect long methods
        split_lines = self.utils.remove_empty_strings_from_list(function_code_blob.strip().splitlines())
        #print(f"Split lines: {split_lines}")
        num_of_lines: int = len(split_lines)
        print(f"Number of lines in the code blob: {num_of_lines}")
        return num_of_lines > 15
    
    def long_parameter_list_detector(self, function_definition: str) -> bool:
        # Detect long parameter lists
        function_definition_arguments: str = function_definition.split("(")[1].split(")")[0]
        parameter_list: list = self.utils.parameter_list_cleanup(function_definition_arguments.split(","))
        print(f"Parameter list: {parameter_list}")
        print(f"Number of parameters: {len(parameter_list)}")
        return len(parameter_list) > 3


if __name__ == "__main__":
    kaun_paada = KaunPaada()
