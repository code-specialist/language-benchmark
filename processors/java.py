from typing import List
import subprocess

from processors.abstract import BenchmarkProcessor


class JavaBenchmarkProcessor(BenchmarkProcessor):

    @staticmethod
    def language() -> str:
        return "Java"

    @staticmethod
    def color() -> str:
        return "#F9690E"

    @classmethod
    def prepare(cls):
        cls.execute(["javac", "implementations/BubbleSort.java"])

    @classmethod
    def process(cls, list_length: int):
        cls.execute(["java", "-cp", "implementations", "BubbleSort", "numbers.txt", str(list_length)])
