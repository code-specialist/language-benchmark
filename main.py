from benchmarks import Benchmarks, BenchmarkConfiguration
from processors import Python311BenchmarkProcessor, JavaBenchmarkProcessor, JavaScriptBenchmarkProcessor, CPPBenchmarkProcessor, Python310BenchmarkProcessor, Python39BenchmarkProcessor

if __name__ == '__main__':
    configuration = BenchmarkConfiguration(
        processors=[
            # Python39BenchmarkProcessor,
            # Python310BenchmarkProcessor,
            # Python311BenchmarkProcessor,
            JavaBenchmarkProcessor,
            JavaScriptBenchmarkProcessor,
            CPPBenchmarkProcessor,
        ],

        # benchmarks
        iterations_per_run=10,
        input_length_max=5000,

        # visualization
        dpi=300,
    )

    benchmarks = Benchmarks(configuration) \
        .run() \
        .visualize() \
        .create_gif()
