from processors.abstract import BenchmarkProcessor


class PythonBenchmarkProcessor(BenchmarkProcessor):

    @staticmethod
    def language() -> str:
        return "Python"

    @staticmethod
    def color() -> str:
        return "#FFD343"

    @classmethod
    def process(cls, list_length: int):
        cls.execute(["venv/bin/python", "implementations/bubblesort.py", "numbers.txt", str(list_length)])
