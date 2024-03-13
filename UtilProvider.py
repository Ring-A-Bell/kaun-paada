import json
import re


class UtilProvider:
    @staticmethod
    def count_lines(code_blob: str) -> int:
        # Count the number of lines in a string
        return len(code_blob.splitlines())

    @staticmethod
    def count_words(code_blob: str) -> int:
        # Count the number of words in a string
        return len(code_blob.split())

    @staticmethod
    def unmarshall_json_object(json_object: str) -> dict:
        # Unmarshall a JSON object
        return json.loads(json_object)

    @staticmethod
    def marshall_json_object(codestring: str) -> str:
        # Marshall a JSON object
        return json.dumps(codestring)

    @staticmethod
    def jaccard_similarity(set1: set, set2: set) -> float:
        # Calculate the Jaccard index of two sets
        return len(set1.intersection(set2)) / len(set1.union(set2))

    @staticmethod
    def parameter_list_cleanup(parameter_list: list) -> list:
        # Clean up the parameter list by stripping and removing type definitions
        return [parameter.strip().split(':')[0] for parameter in parameter_list]

    @staticmethod
    def remove_empty_strings_from_list(string_list: list) -> list:
        # Remove empty strings from a list of strings
        return list(filter(None, string_list))

    @staticmethod
    def is_empty_string(string: str) -> bool:
        # Check if a string has no whitespace characters
        return not string.strip()

    @staticmethod
    def is_import_line(line: str) -> bool:
        # Check if a line is an import line
        return line.startswith("import") or line.startswith("from")

    @staticmethod
    def is_global_const_line(line: str) -> bool:
        # Check if a line is a global constant line
        pattern = re.compile('^[A-Z_]+')
        return True if pattern.match(line) else False

    # Function should be able to preserve the preceding whitespaces
    @staticmethod
    def is_function_definition_line(line: str) -> bool:
        # Check if a line is a function definition line
        pattern = re.compile(r'\s*def')
        return True if pattern.match(line) else False

    @staticmethod
    def is_class_definition_line(line: str) -> bool:
        # Check if a line is a class definition line
        return line.startswith("class")

    @staticmethod
    def is_module_or_script_line(line: str) -> bool:
        # Check if a line is a module or script line
        pattern = re.compile('^if __[a-zA-Z]+__ ==')
        if pattern.match(line):
            return True
        return False

    @staticmethod
    def is_annotation_line(line: str) -> bool:
        # Check if a line is an annotation line
        return line.startswith("@")

    @staticmethod
    def indent_count(line: str) -> int:
        # Count the number of leading spaces in a line
        return len(line) - len(line.lstrip())

    @staticmethod
    def get_ast_args_types(ast_body: any) -> list:
        return [arg.annotation for arg in ast_body.args.args]

    @staticmethod
    def get_ast_args_len(ast_body: any) -> int:
        return len([arg.arg for arg in ast_body.args.args])

    @staticmethod
    def get_ast_return_type(ast_body: any) -> str:
        return ast_body.returns
