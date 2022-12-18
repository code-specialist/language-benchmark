from typing import List
import subprocess

from processors.abstract import BenchmarkProcessor


class JavaBenchmarkProcessor(BenchmarkProcessor):

    @staticmethod
    def language() -> str:
        return "Java"

    @staticmethod
    def prepare():
        subprocess.Popen(
            ["javac", "implementations/BubbleSort.java"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ).communicate()

    @staticmethod
    def process(list_length: int):
        subprocess.Popen(
            ["java", "-cp", "implementations", "BubbleSort", "numbers.txt", str(list_length)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ).communicate()
