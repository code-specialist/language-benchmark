from abc import ABC, abstractmethod
from typing import List


class BenchmarkProcessor(ABC):

    @staticmethod
    @abstractmethod
    def language() -> str:
        pass

    @staticmethod
    @abstractmethod
    def process(list_input: List[int]):
        pass
