from typing import List
import subprocess

from processors.abstract import BenchmarkProcessor


class CPPBenchmarkProcessor(BenchmarkProcessor):

    @staticmethod
    def language() -> str:
        return "C++"

    @staticmethod
    def color() -> str:
        return "#0BB5FF"

    @classmethod
    def prepare(cls):
        cls.execute(["g++", "implementations/bubblesort.cpp", "-o", "implementations/bubblesort-cpp"])

    @classmethod
    def process(cls, list_length: int):
        cls.execute(["./implementations/bubblesort-cpp", "numbers.txt", str(list_length)])
