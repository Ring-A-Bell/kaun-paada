from UtilProvider import UtilProvider

class KaunPaada:
    def __init__(self):
        self.codestring = "def long_parameter_list_detector(self, function_definition: str) -> bool:"
        self.utils = UtilProvider()
        self.long_parameter_list_detector(self.codestring)

    def long_method_detector(self, code_blob: str) -> bool:
        # Detect long methods
        num_of_lines: int = utils.count_lines(code_blob)
        print(f"Number of lines: {num_of_lines}")
        return num_of_lines > 15
    
    def long_parameter_list_detector(self, function_definition: str) -> bool:
        # Detect long parameter lists
        function_definition_arguments: str = function_definition.split("(")[1].split(")")[0]
        parameter_list: list = self.utils.parameter_list_cleanup(function_definition_arguments.split(","))
        print(f"Parameter list: {parameter_list}")
        print(f"Number of parameters: {len(parameter_list)}")
        return len(parameter_list) > 3


if __name__ == "__main__":
    print("Hello World!")
    kaun_paada = KaunPaada()
