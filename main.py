from UtilProvider import utils

class KaunPaada:
    def __init__(self, name):
        self.codestring = ""

    def long_method_detector(self, code_blob: str) -> bool:
        # Detect long methods
        num_of_lines: int = utils.count_lines(code_blob)
        print(f"Number of lines: {num_of_lines}")
        return num_of_lines > 15
    

if __name__ == "__main__":
    print("Hello World!")
