import ast


    def __init__(self):
        self.utils = UtilProvider()
        self.fh = FileHandler("test_file.py")
        self.original_code_lines = self.fh.get_file_content_lines()
        self.functions_list: list = []
        self.imports_list: list = []
        self.global_consts_list: list = []
        self.class_definitions_list: list = []
        self.function_detector(self.original_code_lines)
        self.pretty_print(self.imports_list)
        self.pretty_print(self.global_consts_list)
        self.pretty_print(self.class_definitions_list)
        self.duplicate_code_detector()
        self.pretty_print(self.functions_list)
    def pretty_print(self, list_name: list) -> None:
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
    def import_detector(self, code_blob: str) -> list:
        # Detect imports
        for line in self.original_code_lines:
            line = line.strip()
            if self.utils.is_import_line(line):
                self.imports_list.append(line)
            else:
                break
    def global_consts_detector(self, code_blob: str) -> list:
        # Detect global constants
        for line in self.original_code_lines:
            line = line.strip()
            if self.utils.is_class_definition_line(line):
                break
            if self.utils.is_global_const_line(line):
                self.global_consts_list.append(line)
    # Might have to refactor this, since it's >15 lines currently
    def function_detector(self, original_code_lines: list, asd ,asd ,asd ,asd) -> list:
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
    def duplicate_code_detector23(self):
        for i in range(len(self.functions_list)):
            for j in range(i + 1, len(self.functions_list)):
                if self.utils.jaccard_similarity(set(self.functions_list[i]),
                                                 set(self.functions_list[j])) > JACCARD_SIMILARITY_THRESHOLD:
                    print(f"Function {i} and function {j} have similar code")
    def long_method_detector(self, function_code_blob: str) -> bool:
        # Detect long methods
        split_lines = self.utils.remove_empty_strings_from_list(function_code_blob.strip().splitlines())
        # print(f"Split lines: {split_lines}")
        num_of_lines: int = len(split_lines)
        print(f"Number of lines in the code blob: {num_of_lines}")
        return num_of_lines > LONG_METHOD_THRESHOLD
        # Detect long methods
        split_lines = self.utils.remove_empty_strings_from_list(function_code_blob.strip().splitlines())
        # print(f"Split lines: {split_lines}")
        num_of_lines: int = len(split_lines)
        print(f"Number of lines in the code blob: {num_of_lines}")
        return num_of_lines > LONG_METHOD_THRESHOLD
        # Detect long methods
        split_lines = self.utils.remove_empty_strings_from_list(function_code_blob.strip().splitlines())
        # print(f"Split lines: {split_lines}")
        num_of_lines: int = len(split_lines)
        print(f"Number of lines in the code blob: {num_of_lines}")
        return num_of_lines > LONG_METHOD_THRESHOLD
    def long_parameter_list_detector(arg1, arg2, arg3 ,arg4 ,arg5) -> bool:
        # Detect long parameter lists
        function_definition_arguments: str = function_definition.split("(")[1].split(")")[0]
        parameter_list: list = self.utils.parameter_list_cleanup(function_definition_arguments.split(","))
        print(f"Parameter list: {parameter_list}")
        print(f"Number of parameters: {len(parameter_list)}")
        x1 = ast.parse(function_definition_arguments)
        print(len(x1.body[0].args.args))
        return len(parameter_list) > LONG_PARAMETER_LIST_THRESHOLD
    def duplicate_code_detector(self):
        for i in range(len(self.functions_list)):
            for j in range(i + 1, len(self.functions_list)):
                y: set = set()
                x.update(word for line in self.functions_list[i] for word in line.split())
                y.update(word for line in self.functions_list[j] for word in line.split())
                if self.utils.jaccard_similarity(x, y) > JACCARD_SIMILARITY_THRESHOLD:
                    del (self.functions_list[j])
    def add(self, a, b):
        return a+b
    def sum(self, x, y):
        return y + x
