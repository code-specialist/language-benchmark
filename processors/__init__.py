from processors.cpp import CPPBenchmarkProcessor
from processors.java import JavaBenchmarkProcessor
from processors.javascript import JavaScriptBenchmarkProcessor
from processors.python import Python311BenchmarkProcessor, Python39BenchmarkProcessor, Python310BenchmarkProcessor

__all__ = [
    Python311BenchmarkProcessor,
    Python310BenchmarkProcessor,
    Python39BenchmarkProcessor,
    JavaBenchmarkProcessor,
    JavaScriptBenchmarkProcessor,
    CPPBenchmarkProcessor,
]
