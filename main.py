import ast
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
        self.long_methods_dict: dict = {}
        self.long_parameter_list_dict: dict = {}
        self.duplicate_functions_list: list = []

        self.function_detector()

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
    def pre_function_detector(self) -> None:
        for line in self.original_code_lines:
            # Should extract these conditions into a separate function
            if self.utils.is_import_line(line):
                self.imports_list.append(line)
            elif self.utils.is_global_const_line(line):
                self.global_consts_list.append(line)
            elif self.utils.is_class_definition_line(line):
                self.class_definitions_list.append(line)
            elif self.utils.is_empty_string(line):
                continue
            break

    def function_detector(self) -> None:
        new_function_flag: bool = False
        current_function: list = []
        self.pre_function_detector()
        for line in self.original_code_lines:
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

    def long_method_detector(self) -> dict:
        # Detect long methods
        for _function in self.functions_list:
            _function = self.utils.remove_empty_strings_from_list(_function)
            if len(_function) > LONG_METHOD_THRESHOLD:
                self.long_methods_dict.update({_function[0]: len(_function)})
        return self.long_methods_dict

    def long_parameter_list_detector(self) -> dict:
        # Detect long parameter lists
        for function in self.functions_list:
            param_nums = self.utils.get_ast_args_len(self.parse_ast(function))
            if param_nums > LONG_PARAMETER_LIST_THRESHOLD:
                self.long_parameter_list_dict.update({function[0]: param_nums})
        return self.long_parameter_list_dict

    def duplicate_code_detector(self) -> list:
        function_list_copy = list()
        duplicate_functions_list = list()
        for i in range(len(self.functions_list)):
            x: set = set()
            for j in range(i + 1, len(self.functions_list)):
                y: set = set()
                x.update(word for line in self.functions_list[i] for word in line.split())
                y.update(word for line in self.functions_list[j] for word in line.split())
                if self.utils.jaccard_similarity(x, y) > JACCARD_SIMILARITY_THRESHOLD:
                    function_list_copy.append(self.functions_list[j])
                    duplicate_functions_list.append(f"Functions {i} and {j} have similar code")
        self.functions_list = [function for function in self.functions_list if function not in function_list_copy]
        return duplicate_functions_list

    def refactor_file(self, filepath: str) -> None:
        self.fh.refactor_file(self.imports_list, self.global_consts_list, self.class_definitions_list,
                              self.functions_list)
        self.fh.save_file(filepath)

    def extract_operators(self, node) -> list:
        if isinstance(node, ast.BinOp):
            return [type(node.op)] + self.extract_operators(node.left) + self.extract_operators(node.right)
        elif isinstance(node, ast.AST):
            return [value for field, value in ast.iter_fields(node) if isinstance(value, ast.AST)]
        elif isinstance(node, list):
            return [item for sublist in node for item in self.extract_operators(sublist)]
        return []

    def parse_ast(self, code: list) -> ast.stmt:
        indent_level = self.utils.indent_count(code[0])
        code = [line[indent_level:] for line in code]
        return ast.parse("\n".join(code)).body[0]

    def compare_code(self, ast1: any, ast2: any) -> bool:
        if self.utils.get_ast_args_len(ast1) != self.utils.get_ast_args_len(ast2):
            return False
        if self.utils.get_ast_args_types(ast1) != self.utils.get_ast_args_types(ast2):
            return False
        if self.utils.get_ast_return_type(ast1) != self.utils.get_ast_return_type(ast2):
            return False
        if self.extract_operators(getattr(ast1.body[0], 'value', None)) != self.extract_operators(
                getattr(ast2.body[0], 'value', None)):
            return False
        return True

    def semantic_code_detector(self) -> list:
        # Detect semantic equality based on parameters, return type and operators
        semantically_equal_functions = []
        function_list_copy = list()
        for i in range(len(self.functions_list) - 1):
            for j in range(i + 1, len(self.functions_list)):
                if self.compare_code(self.parse_ast(self.functions_list[i]), self.parse_ast(self.functions_list[j])):
                    semantically_equal_functions.append(f"Functions {i} and {j} are semantically equal")
                    function_list_copy.append(self.functions_list[j])
        self.functions_list = [function for function in self.functions_list if function not in function_list_copy]
        return semantically_equal_functions


if __name__ == "__main__":
    kaun_paada = KaunPaada("test_file.py")
