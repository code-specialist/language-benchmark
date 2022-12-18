import subprocess
from abc import ABC, abstractmethod
from typing import List


class BenchmarkProcessor(ABC):

    @staticmethod
    @abstractmethod
    def language() -> str:
        pass

    @staticmethod
    @abstractmethod
    def color() -> str:
        pass

    @classmethod
    def prepare(cls):
        pass

    @classmethod
    @abstractmethod
    def process(cls, list_length: int):
        pass

    @staticmethod
    def execute(command: List[str]):
        subprocess.check_call(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
