import json
import statistics
from collections import defaultdict
from time import perf_counter
from typing import Dict, List

from processors import PythonBenchmarkProcessor, JavaBenchmarkProcessor, CPPBenchmarkProcessor, JavaScriptBenchmarkProcessor


class Benchmarks:

    def __init__(self, runs: int, list_length_min: int = 100, list_length_max: int = 100000, tries_per_run: int = 30):
        self.list_length_min = list_length_min
        self.list_length_max = list_length_max
        self.runs = runs
        self.tries_per_run = tries_per_run
        self.results: Dict[str, List[float]] = defaultdict(lambda: [])
        self.language_processors = [
            PythonBenchmarkProcessor,
            JavaBenchmarkProcessor,
            JavaScriptBenchmarkProcessor,
            CPPBenchmarkProcessor,
        ]

    def run(self):
        print("\nPreparing Benchmarks...")
        for processor in self.language_processors:
            processor.prepare()
        print("Benchmarks prepared, let's go!")

        print(f"\nStarting Benchmarks - {self.runs} runs")

        for list_length in range(self.list_length_min, self.list_length_max, int(self.list_length_max / self.runs)):
            print(f"\n\t Run {int(list_length / int(self.list_length_max / self.runs)) + 1}:")
            for processor in self.language_processors:

                tries = []
                for _ in range(self.tries_per_run):
                    start = perf_counter()
                    processor.process(list_length=list_length)
                    end = perf_counter()
                    tries.append(end - start)

                average_processing_time = statistics.mean(tries)
                print(f"\t\t[{processor.language()}] - {average_processing_time} seconds")

                self.results[processor.language()].append(average_processing_time)

        print("Benchmarks finished!\n")

    def export(self, filename: str):
        with open(filename, "w") as file:
            json.dump(self.results, file)
