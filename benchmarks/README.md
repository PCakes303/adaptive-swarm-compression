# Benchmarks

The benchmark suite will compare raw bytes, established codecs, and candidate pipelines across declared workload classes. The first executable benchmark should report source bytes, encoded bytes, encode/decode time, and exact reconstruction. Later versions must include metadata, dictionaries, indexes, transfer, coordination, and recovery costs.

Do not interpret a single compression ratio as total system improvement. Record Python version, platform, codec version, input generator, and random seed.
