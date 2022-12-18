from typing import List
import subprocess

from processors.abstract import BenchmarkProcessor


class CPPBenchmarkProcessor(BenchmarkProcessor):

    @staticmethod
    def language() -> str:
        return "C++"

    @staticmethod
    def prepare():
        subprocess.Popen(
            ["g++", "implementations/bubblesort.cpp", "-o", "implementations/bubblesort-cpp"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ).communicate()

    @staticmethod
    def process(list_length: int):
        subprocess.Popen(
            ["./implementations/bubblesort-cpp", "numbers.txt", str(list_length)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ).communicate()
