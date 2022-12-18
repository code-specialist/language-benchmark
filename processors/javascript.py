import subprocess

from processors.abstract import BenchmarkProcessor


class JavaScriptBenchmarkProcessor(BenchmarkProcessor):

    @staticmethod
    def language() -> str:
        return "JavaScript"

    @staticmethod
    def prepare():
        pass

    @staticmethod
    def process(list_length: int):
        subprocess.Popen(
            ["node", " implementations/bubblesort.js", "numbers.txt", str(list_length)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ).communicate()
