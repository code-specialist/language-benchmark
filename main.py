from benchmarks import Benchmarks
from visualize import BenchmarkVisualizer

if __name__ == '__main__':
    benchmarks = Benchmarks(list_length_min=0, list_length_max=50000, iterations=100, tries_per_iteration=15)
    benchmarks.run()
    benchmarks.export("results.json")

    visualizer = BenchmarkVisualizer(benchmarks=benchmarks.results)
    visualizer.visualize()
    visualizer.create_gif()
