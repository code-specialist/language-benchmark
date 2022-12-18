from benchmarks import Benchmarks
from visualize import BenchmarkVisualizer

if __name__ == '__main__':
    benchmarks = Benchmarks(runs=100, list_length_max=1000, tries_per_run=50)
    benchmarks.run()

    visualizer = BenchmarkVisualizer(benchmarks=benchmarks.results)
    visualizer.visualize()
    visualizer.create_gif()
