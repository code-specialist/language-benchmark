from io import BytesIO
from typing import Dict, List

import matplotlib.pyplot as plt
from PIL import Image


class BenchmarkVisualizer:

    def __init__(self, benchmarks: Dict[str, List[float]]):
        self.benchmarks = benchmarks
        self.frames = []
        self.language_color_mapping = {
            "Python": "#FFD343",
            "Java": "#FF0000",
        }

    def visualize(self):
        print("Starting Data Visualization...")

        plots: Dict[str, List[float]] = {}
        total_width = len(tuple(self.benchmarks.values())[0])

        def visualize_step():
            bytes_object = BytesIO()
            plt.figure(facecolor="#111827")  # Background Color

            plt.xlim(0, total_width)
            plt.ylim(0, .5)

            for lang, points in plots.items():
                points_to_plot = [*points, *([None for _ in range(total_width - len(points))])]
                plt.plot(range(total_width), points_to_plot, self.language_color_mapping[lang], label=lang)  # Create a bar chart using the current values of input_list

            plt.tight_layout()  # Make it use tight layout to reduce borders and margins
            plt.axis('off')  # Remove axis
            plt.savefig(bytes_object)  # Save the plot in-memory
            plt.close("all")  # Ensure everything from pyplot gets closed, to save memory

            self.frames.append(Image.open(bytes_object))  # Append the frame path to the frame list

        for language, benchmark_times in self.benchmarks.items():
            for index in range(len(benchmark_times)):
                plots[language] = benchmark_times[:index + 1]
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

        # with imageio.get_writer("animation.gif", mode='I', duration=1 / 30) as writer:
        #     # Write images where each is display for 1/30s → 30 frames per second
        #     for frame in self.frames:  # Iterate over the frames
        #         frame = imread(frame)  # Convert to ndarray
        #         writer.append_data(frame)  # Write the image to the stream

        print("Successfully created GIF!")
