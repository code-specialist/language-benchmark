from processors.abstract import BenchmarkProcessor


class JavaScriptBenchmarkProcessor(BenchmarkProcessor):

    @staticmethod
    def language() -> str:
        return "JavaScript"

    @staticmethod
    def color() -> str:
        return "#84BA64"

    @classmethod
    def process(cls, list_length: int):
        cls.execute(["node", "implementations/bubblesort.js", "numbers.txt", str(list_length)])
