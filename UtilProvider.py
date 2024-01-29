import json

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
    
    def jaccard_index(self, set1: set, set2: set) -> float:
        # Calculate the Jaccard index of two sets
        return len(set1.intersection(set2)) / len(set1.union(set2))
    
    def parameter_list_cleanup(self, parameter_list: list) -> list:
        # Clean up the parameter list by stripping and removing type definitions
        return [parameter.strip().split(':')[0] for parameter in parameter_list]
