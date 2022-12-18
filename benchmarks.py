import json
import sys
from collections import defaultdict
from random import randint
from time import perf_counter
from typing import Dict, List
import statistics

from processors import PythonBenchmarkProcessor, JavaBenchmarkProcessor


class Benchmarks:

    def __init__(self, list_length_min: int, list_length_max: int, iterations: int, tries_per_iteration: int = 30):
        self.list_length_min = list_length_min
        self.list_length_max = list_length_max
        self.iterations = iterations
        self.tries_per_iteration = tries_per_iteration
        self.results: Dict[str, List[float]] = defaultdict(lambda: [])
        self.language_processors = [
            PythonBenchmarkProcessor,
            JavaBenchmarkProcessor,
        ]

    def run(self):
        print("\nPreparing Benchmarks...")
        for processor in self.language_processors:
            processor.prepare()
        print("Benchmarks prepared, let's go!")

        print(f"\nStarting Benchmarks - {self.iterations} iterations")

        sys.setrecursionlimit(10000)

        for list_length in range(self.list_length_min, self.list_length_max, int(self.list_length_max / self.iterations)):
            list_to_sort = [randint(self.list_length_min, self.list_length_max) for _ in range(list_length)]

            for processor in self.language_processors:
                print(f"\t[{processor.language()}] iteration {int(list_length / int(self.list_length_max / self.iterations)) + 1}")

                tries = []
                for _ in range(self.tries_per_iteration):
                    start = perf_counter()
                    processor.process(list_input=list_to_sort)
                    end = perf_counter()
                    tries.append(end - start)

                self.results[processor.language()].append(statistics.mean(tries))

        print("Benchmarks finished!\n")

    def export(self, filename: str):
        with open(filename, "w") as file:
            json.dump(self.results, file)
