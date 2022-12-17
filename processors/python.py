from typing import List
import subprocess

from processors.abstract import BenchmarkProcessor


class PythonBenchmarkProcessor(BenchmarkProcessor):

    @staticmethod
    def language() -> str:
        return "Python"

    @staticmethod
    def process(list_input: List[int]):
        process = subprocess.Popen(
            ['venv/bin/python', 'implementations/python.py', f'"{list_input}"'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        process.communicate()
