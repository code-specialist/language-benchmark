from benchmarks import Benchmarks, BenchmarkConfiguration
from processors import PythonBenchmarkProcessor, JavaBenchmarkProcessor, JavaScriptBenchmarkProcessor, CPPBenchmarkProcessor

if __name__ == '__main__':
    configuration = BenchmarkConfiguration(
        processors=[
            PythonBenchmarkProcessor,
            JavaBenchmarkProcessor,
            JavaScriptBenchmarkProcessor,
            CPPBenchmarkProcessor,
        ],

        # benchmarks
        iterations_per_run=1,
        input_length_max=1000,

        # visualization
        dpi=50,
    )

    benchmarks = Benchmarks(configuration) \
        .run() \
        .visualize() \
        .create_gif()
