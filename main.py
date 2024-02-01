from UtilProvider import UtilProvider
from FileHandler import FileHandler

LONG_METHOD_THRESHOLD: int = 15
LONG_PARAMETER_LIST_THRESHOLD: int = 3
JACCARD_SIMILARITY_THRESHOLD: float = 0.75
LINE_BREAK_PRINT: str = "#" + "-"*50 + "#"

class KaunPaada:
    def __init__(self, file_path: str):
        print(f"File path: {file_path}")
        self.utils = UtilProvider()
        self.fh = FileHandler(file_path)
        self.original_code_lines = self.fh.get_file_content_lines()
        self.functions_list: list = []
        self.imports_list: list = []
        self.global_consts_list: list = []
        self.class_definitions_list: list = []
        self.long_methods_list: list = []
        self.long_parameter_list_functions: list = []

        self.function_detector()
        #self.pretty_print(self.imports_list)
        #self.pretty_print(self.global_consts_list)
        #self.pretty_print(self.class_definitions_list)
        self.duplicate_code_detector()
        self.pretty_print(self.functions_list)
        #self.refactor_file("refactored_file.py")

    @staticmethod
    def pretty_print(list_name: list) -> None:
        if not list_name:
            return
        if isinstance(list_name[0], list):
            for item in list_name:
                for line in item:
                    print(line)
                print(LINE_BREAK_PRINT)
        else:
            for item in list_name:
                print(item)
            print(LINE_BREAK_PRINT)

    def import_detector(self) -> None:
        # Detect imports
        for line in self.original_code_lines:
            if self.utils.is_import_line(line.strip()):
                self.imports_list.append(line.strip())
            else:
                break

    def global_consts_detector(self) -> None:
        # Detect global constants
        for line in self.original_code_lines:
            if self.utils.is_class_definition_line(line.strip()):
                break
            if self.utils.is_global_const_line(line):
                self.global_consts_list.append(line)

    # Might have to refactor this, since it's >15 lines currently
    def function_detector(self) -> list:
        new_function_flag: bool = False
        current_function: list = []
        for line in self.original_code_lines:
            # Should extract these conditions into a separate function
            if self.utils.is_import_line(line):
                self.imports_list.append(line)
            elif self.utils.is_global_const_line(line):
                self.global_consts_list.append(line)
            elif self.utils.is_class_definition_line(line):
                self.class_definitions_list.append(line)
            if self.utils.is_empty_string(line):
                continue
            elif self.utils.is_function_definition_line(line) or self.utils.is_module_or_script_line(line):
                if new_function_flag:
                    self.functions_list.append(current_function)
                    current_function = []
                new_function_flag = True
                current_function.append(line)
            else:
                if current_function:
                    current_function.append(line)
        if current_function not in self.functions_list:
                self.functions_list.append(current_function)

    def long_method_detector(self) -> list:
        # Detect long methods
        for function in self.functions_list:
            function = self.utils.remove_empty_strings_from_list(function)
            if len(function) > LONG_METHOD_THRESHOLD:
                self.long_methods_list.append(function[0])
        return self.long_methods_list

    # def long_method_detector(self, function_code_blob: str) -> bool:
    #     # Detect long methods
    #     split_lines = self.utils.remove_empty_strings_from_list(function_code_blob.strip().splitlines())
    #     #print(f"Split lines: {split_lines}")
    #     num_of_lines: int = len(split_lines)
    #     print(f"Number of lines in the code blob: {num_of_lines}")
    #     return num_of_lines > LONG_METHOD_THRESHOLD

    def long_parameter_list_detector(self) -> list:
        # Detect long parameter lists
        for function in self.functions_list:
            function_definition_arguments: str = function[0].split("(")[1].split(")")[0]
            parameter_list: list = self.utils.parameter_list_cleanup(function_definition_arguments.split(","))
            if len(parameter_list) > LONG_PARAMETER_LIST_THRESHOLD:
                self.long_parameter_list_functions.append(function[0])
        return self.long_parameter_list_functions

    # def long_parameter_list_detector(self, function_definition: str) -> bool:
    #     # Detect long parameter lists
    #     function_definition_arguments: str = function_definition.split("(")[1].split(")")[0]
    #     parameter_list: list = self.utils.parameter_list_cleanup(function_definition_arguments.split(","))
    #     print(f"Parameter list: {parameter_list}")
    #     print(f"Number of parameters: {len(parameter_list)}")
    #     return len(parameter_list) > LONG_PARAMETER_LIST_THRESHOLD

    def duplicate_code_detector(self):
        function_list_copy = list()
        for i in range(len(self.functions_list)):
            x: set = set()
            for j in range(i + 1, len(self.functions_list)):
                y: set = set()
                x.update(word for line in self.functions_list[i] for word in line.split())
                y.update(word for line in self.functions_list[j] for word in line.split())
                if self.utils.jaccard_similarity(x, y) > JACCARD_SIMILARITY_THRESHOLD:
                    function_list_copy.append(self.functions_list[j])
        self.functions_list = [function for function in self.functions_list if function not in function_list_copy]

    def refactor_file(self, filepath: str) -> None:
        self.fh.refactor_file(self.imports_list, self.global_consts_list, self.class_definitions_list, self.functions_list)
        self.fh.save_file(filepath)


if __name__ == "__main__":
    kaun_paada = KaunPaada("test_file.py")
