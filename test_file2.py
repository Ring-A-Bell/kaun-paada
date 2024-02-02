import ast

from UtilProvider import UtilProvider
from FileHandler import FileHandler

LONG_METHOD_THRESHOLD: int = 15
LONG_PARAMETER_LIST_THRESHOLD: int = 3
JACCARD_SIMILARITY_THRESHOLD: float = 0.75
LINE_BREAK_PRINT: str = "#" + "-" * 50 + "#"


class KaunPaada:
    def add(self, a, b):
        return a + b

    def sum(self, x, y):
        return x + y