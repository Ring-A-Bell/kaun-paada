from UtilProvider import UtilProvider

class KaunPaada:
    def __init__(self):
        self.codestring = "def long_parameter_list_detector(self, function_definition: str) -> bool:\n\nasd\nline"
        self.utils = UtilProvider()
        print(self.long_method_detector(self.codestring))
        print(self.long_parameter_list_detector(self.codestring))

    def long_method_detector(self, function_code_blob: str) -> bool:
        # Detect long methods
        split_lines = self.utils.remove_empty_strings_from_list(function_code_blob.strip().splitlines())
        print(f"Split lines: {split_lines}")
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
