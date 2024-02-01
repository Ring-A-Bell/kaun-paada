import json
import re

class UtilProvider:
    def count_lines(self, code_blob: str) -> int:
        # Count the number of lines in a string
        return len(code_blob.splitlines())
    
    def count_words(self, code_blob: str) -> int:
        # Count the number of words in a string
        return len(code_blob.split())
    
    def unmarshall_json_object(self, json_object: str) -> dict:
        # Unmarshall a JSON object
        return json.loads(json_object)
    
    def marshall_json_object(self, codestring: str) -> str:
        # Marshall a JSON object
        return json.dumps(codestring)
    
    def jaccard_similarity(self, set1: set, set2: set) -> float:
        # Calculate the Jaccard index of two sets
        return len(set1.intersection(set2)) / len(set1.union(set2))
    
    def parameter_list_cleanup(self, parameter_list: list) -> list:
        # Clean up the parameter list by stripping and removing type definitions
        return [parameter.strip().split(':')[0] for parameter in parameter_list]
    
    def remove_empty_strings_from_list(self, string_list: list) -> list:
        # Remove empty strings from a list of strings
        return list(filter(None, string_list))
    
    def is_empty_string(self, string: str) -> bool:
        # Check if a string has no whitespace characters
        return not string.strip()
    
    def is_import_line(self, line: str) -> bool:
        # Check if a line is an import line
        return line.startswith("import") or line.startswith("from")

    def is_global_const_line(self, line: str) -> bool:
        # Check if a line is a global constant line
        pattern = re.compile('^[A-Z_]+')
        return True if pattern.match(line) else False
    
    # Function should be able to preserve the preceding whitespaces
    def is_function_definition_line(self, line: str) -> bool:
        # Check if a line is a function definition line
        pattern  = re.compile('\s*def')
        return True if pattern.match(line) else False
        #return line.startswith("def")
    
    def is_class_definition_line(self, line: str) -> bool:
        # Check if a line is a class definition line
        return line.startswith("class")
    
    def is_module_or_script_line(self, line: str) -> bool:
        # Check if a line is a module or script line
        pattern = re.compile('^if __[a-zA-Z]+__ ==')
        if pattern.match(line):
            return True
        return False
    


"""
Cannot change the execution of the function (preserve functionality)
post refactoring, it has to have - 

changed internal structure without changing the external behavior

same i/p and o/p

"""