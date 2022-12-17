from typing import List
import subprocess

from processors.abstract import BenchmarkProcessor


class JavaBenchmarkProcessor(BenchmarkProcessor):

    @staticmethod
    def language() -> str:
        return "Java"

    @staticmethod
    def process(list_input: List[int]):
        process = subprocess.Popen(
            ['java', 'implementations/bubblesort', *map(str, list_input)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        process.communicate()
