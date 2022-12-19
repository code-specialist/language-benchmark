import statistics
import sys
from collections import defaultdict
from dataclasses import dataclass
from functools import lru_cache
from io import BytesIO
from math import ceil, floor
from time import perf_counter
from typing import Dict, List, Type, Self

from PIL import Image
from matplotlib import pyplot as plt

from processors.abstract import BenchmarkProcessor


@dataclass
class BenchmarkConfiguration:
    processors: list[Type[BenchmarkProcessor]]

    # benchmarks
    runs: int = 30
    iterations_per_run: int = 10
    input_length_min: int = 100
    input_length_max: int = 10000

    # visualization
    background_color: str = "#111827"
    dpi: int = 150


class Benchmarks:

    def __init__(self, configuration: BenchmarkConfiguration):
        self.configuration = configuration
        self._results: dict[Type[BenchmarkProcessor], list[float]] = defaultdict(lambda: [])
        self._frames = []

    def run(self) -> Self:
        print("\nPreparing Benchmarks...")
        for processor in self.configuration.processors:
            processor.prepare()
        print("Benchmarks prepared, let's go!\n")

        run_counter, step_width = 0, ceil((self.configuration.input_length_max - self.configuration.input_length_min) / self.configuration.runs)
        for list_length in range(self.configuration.input_length_min, self.configuration.input_length_max, step_width):
            if run_counter > self.configuration.runs:
                break

            processor_counter = 0
            run_counter += 1

            def display_progress():
                self._display_benchmark_progress(
                    run=run_counter,
                    current_step=(run_counter - 1) * len(self.configuration.processors) + processor_counter,
                    total_steps=self.configuration.runs * len(self.configuration.processors),
                    current_language=processor.language(),
                )

            for processor in self.configuration.processors:
                tries = []

                display_progress()

                for _ in range(self.configuration.iterations_per_run):
                    start = perf_counter()
                    processor.process(list_length=list_length)
                    end = perf_counter()
                    tries.append(end - start)

                average_processing_time = statistics.mean(tries)
                processor_counter += 1

                self._results[processor].append(average_processing_time)

                display_progress()

        print("\nBenchmarks finished!\n")

        return self

    def visualize(self) -> Self:
        if not self._results:
            raise ValueError("Could not visualize Benchmarks, they didn't run yet")

        plots: Dict[Type[BenchmarkProcessor], List[float]] = {}
        total_width = len(tuple(self._results.values())[0])
        total_frames = total_width * len(self._results.keys()) * 2

        def visualize_step():
            bytes_object = BytesIO()

            plt.figure(facecolor=self.configuration.background_color, dpi=self.configuration.dpi)
            plt.xlim(0, total_width)
            plt.ylim(0, self._get_longest_run() * 1.1)

            for processor, points in plots.items():
                points_to_plot = [*points, *([None for _ in range(total_width - len(points))])]
                plt.plot(range(total_width), points_to_plot, processor.color(), label=processor.language())

            plt.tight_layout()
            plt.axis("off")
            plt.legend(loc="upper left", facecolor=self.configuration.background_color, labelcolor="white", frameon=False)
            plt.savefig(bytes_object)
            plt.close("all")

            self._frames.append(Image.open(bytes_object))
            self._display_visualization_progress(current_frame=len(self._frames), total_frames=total_frames)

        for language, benchmark_times in self._results.items():
            for index in range(len(benchmark_times)):
                plots[language] = benchmark_times[:index + 1]
                visualize_step()

        for _ in range(int(len(self._frames))):
            visualize_step()

        print("\nData Visualization finished!\n")

        return self

    def create_gif(self) -> Self:
        if not self._frames:
            raise ValueError("Could not create GIF - Benchmarks aren't visualized")

        print("Creating GIF...")

        frame_one = self._frames[0]
        frame_one.save(
            "benchmark.gif",
            format="GIF",
            append_images=self._frames,
            save_all=True,
            duration=30,
            loop=0,
        )

        print("Successfully created GIF!")

        return self

    @property
    def results(self) -> dict[Type[BenchmarkProcessor], list[float]]:
        return self._results

    def _display_benchmark_progress(self, run: int, current_step: int, total_steps: int, current_language: str, bar_length=50) -> None:
        progress = current_step / total_steps
        bar = self._progress_bar_str(progress=progress, width=bar_length)
        language = self._current_language_str(current_language=current_language)
        run_progress = self._benchmark_run_progress_str(run=run)
        progress_percent = round(progress * 100, 1)
        sys.stdout.write(f'Running Benchmarks | Run {run_progress} {language} - {bar} {progress_percent}%\r')
        sys.stdout.flush()

    def _display_visualization_progress(self, current_frame: int, total_frames: int, bar_length=50) -> None:
        progress = current_frame / total_frames
        bar = self._progress_bar_str(progress=progress, width=bar_length)
        progress_percent = round(progress * 100, 1)
        sys.stdout.write(f'Visualizing Benchmarks - {bar} {progress_percent}%\r')
        sys.stdout.flush()

    @staticmethod
    def _progress_bar_str(progress: float, width: int) -> str:
        progress = min(1., max(0., progress))
        whole_width = floor(progress * width)
        remainder_width = (progress * width) % 1
        part_width = floor(remainder_width * 8)
        part_char = [" ", "▏", "▎", "▍", "▌", "▋", "▊", "▉"][part_width]
        if (width - whole_width - 1) < 0:
            part_char = ""
        line = "█" * whole_width + part_char + " " * (width - whole_width - 1)
        return line

    def _benchmark_run_progress_str(self, run: int) -> str:
        max_run_digits = len(str(self.configuration.runs))
        current_run_digits = len(str(run))
        return f'{"0" * (max_run_digits - current_run_digits)}{run}/{self.configuration.runs}'

    @lru_cache()
    def _current_language_str(self, current_language: str) -> str:
        languages = [processor.language() for processor in self.configuration.processors]
        max_language_character_size = max(map(len, languages))
        current_language_character_size = len(current_language)
        return f'[{current_language}]{" " * (max_language_character_size - current_language_character_size)}'

    def _get_longest_run(self) -> float:
        longest_run = 0
        for benchmarks in self._results.values():
            longest_run = max(longest_run, max(benchmarks))
        return longest_run
