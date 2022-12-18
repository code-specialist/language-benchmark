import json
import statistics
from collections import defaultdict
from time import perf_counter
from typing import Dict, List, Type

from processors.abstract import BenchmarkProcessor


class Benchmarks:

    def __init__(self, processors: List[Type[BenchmarkProcessor]], runs: int, tries_per_run: int = 30, list_length_min: int = 100, list_length_max: int = 100000):
        self.list_length_min = list_length_min
        self.list_length_max = list_length_max
        self.runs = runs
        self.tries_per_run = tries_per_run
        self.results: Dict[Type[BenchmarkProcessor], List[float]] = defaultdict(lambda: [])
        self.processors = processors

    def run(self):
        print("\nPreparing Benchmarks...")
        for processor in self.processors:
            processor.prepare()
        print("Benchmarks prepared, let's go!")

        print(f"\nStarting Benchmarks - {self.runs} runs")

        run_counter = 0
        for list_length in range(self.list_length_min, self.list_length_max, int((self.list_length_max - self.list_length_min) / self.runs)):
            run_counter += 1
            print(f"\n\t Run {run_counter}")
            for processor in self.processors:

                tries = []
                for _ in range(self.tries_per_run):
                    start = perf_counter()
                    processor.process(list_length=list_length)
                    end = perf_counter()
                    tries.append(end - start)

                average_processing_time = statistics.mean(tries)
                print(f"\t\t[{processor.language()}] - {average_processing_time} seconds")

                self.results[processor].append(average_processing_time)

        print("\nBenchmarks finished!\n")

    def export(self, filename: str):
        with open(filename, "w") as file:
            json.dump(self.results, file)
