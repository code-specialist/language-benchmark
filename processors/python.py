import subprocess

from processors.abstract import BenchmarkProcessor


class PythonBenchmarkProcessor(BenchmarkProcessor):

    @staticmethod
    def language() -> str:
        return "Python"

    @staticmethod
    def prepare():
        pass

    @staticmethod
    def process(list_length: int):
        subprocess.Popen(
            ["venv/bin/python", "implementations/bubblesort.py", "numbers.txt", str(list_length)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ).communicate()
