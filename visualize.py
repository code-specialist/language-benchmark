from io import BytesIO
from typing import Dict, List, Type

import matplotlib.pyplot as plt
from PIL import Image

from processors.abstract import BenchmarkProcessor


class BenchmarkVisualizer:
    background_color = "#111827"

    def __init__(self, benchmarks: Dict[Type[BenchmarkProcessor], List[float]]):
        self.benchmarks = benchmarks
        self.frames = []

    def visualize(self):
        print("Starting Data Visualization...")

        plots: Dict[Type[BenchmarkProcessor], List[float]] = {}
        total_width = len(tuple(self.benchmarks.values())[0])

        def visualize_step():
            bytes_object = BytesIO()
            plt.figure(facecolor=self.background_color)  # Background Color

            plt.xlim(0, total_width)
            plt.ylim(0, self._get_longest_run() * 1.1)

            for processor, points in plots.items():
                points_to_plot = [*points, *([None for _ in range(total_width - len(points))])]
                plt.plot(range(total_width), points_to_plot, processor.color(), label=processor.language())  # Create a bar chart using the current values of input_list

            plt.tight_layout()  # Make it use tight layout to reduce borders and margins
            plt.axis('off')  # Remove axis
            plt.savefig(bytes_object)  # Save the plot in-memory
            plt.close("all")  # Ensure everything from pyplot gets closed, to save memory

            self.frames.append(Image.open(bytes_object))  # Append the frame path to the frame list

        for language, benchmark_times in self.benchmarks.items():
            for index in range(len(benchmark_times)):
                plots[language] = benchmark_times[:index + 1]
                visualize_step()

        for _ in range(int(len(self.frames) * .5)):
            visualize_step()

        print("Data Visualization finished!\n")

    def create_gif(self):
        print("Creating GIF...")

        frame_one = self.frames[0]
        frame_one.save(
            "benchmark.gif",
            format="GIF",
            append_images=self.frames,
            save_all=True,
            duration=30,
            loop=0,
        )

        print("Successfully created GIF!")

    def _get_longest_run(self) -> float:
        longest_run = 0
        for benchmarks in self.benchmarks.values():
            longest_run = max(longest_run, max(benchmarks))
        return longest_run
