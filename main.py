from benchmarks import Benchmarks
from processors import PythonBenchmarkProcessor, JavaBenchmarkProcessor, JavaScriptBenchmarkProcessor, CPPBenchmarkProcessor
from visualize import BenchmarkVisualizer

if __name__ == '__main__':
    processors = [
        PythonBenchmarkProcessor,
        JavaBenchmarkProcessor,
        JavaScriptBenchmarkProcessor,
        CPPBenchmarkProcessor,
    ]

    benchmarks = Benchmarks(processors=processors, runs=30, tries_per_run=3, list_length_max=1000)
    benchmarks.run()

    visualizer = BenchmarkVisualizer(benchmarks=benchmarks.results)
    visualizer.visualize()
    visualizer.create_gif()
