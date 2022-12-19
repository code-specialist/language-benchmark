from abc import ABC, abstractmethod

from processors.abstract import BenchmarkProcessor


class PythonBaseBenchmarkProcessor(BenchmarkProcessor, ABC):
    @staticmethod
    @abstractmethod
    def python_version() -> str:
        raise NotImplementedError

    @classmethod
    def language(cls) -> str:
        return f"Python {cls.python_version()}"

    @staticmethod
    def color() -> str:
        return "#FFD343"

    @classmethod
    def process(cls, list_length: int):
        cls.execute([f"python{cls.python_version()}", "implementations/bubblesort.py", "numbers.txt", str(list_length)])


class Python311BenchmarkProcessor(PythonBaseBenchmarkProcessor):
    @staticmethod
    def python_version() -> str:
        return "3.11"

    @staticmethod
    def color() -> str:
        return "#ffff66"


class Python310BenchmarkProcessor(PythonBaseBenchmarkProcessor):

    @staticmethod
    def python_version() -> str:
        return "3.10"

    @staticmethod
    def color() -> str:
        return "#ffd700"


class Python39BenchmarkProcessor(PythonBaseBenchmarkProcessor):

    @staticmethod
    def python_version() -> str:
        return "3.9"

    @staticmethod
    def color() -> str:
        return "#ff8c00"
