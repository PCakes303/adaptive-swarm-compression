"""Run local identity-versus-zlib benchmarks and emit machine-readable JSON."""

import argparse
import json
import platform
import sys
import time
import tracemalloc

from adaptive_swarm_compression import PipelineStage, decode_pipeline, encode_pipeline
from benchmarks.workloads import build_workloads


def _measure_peak(callable_object):
    tracemalloc.start()
    started = time.perf_counter_ns()
    result = callable_object()
    elapsed = time.perf_counter_ns() - started
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return result, elapsed, peak


def benchmark_one(name: str, source: bytes, codec: str) -> dict:
    parameters = {"level": 6} if codec == "zlib" else {}
    version = "rfc1950-1" if codec == "zlib" else "1"
    stage = PipelineStage(codec, version, parameters)

    artifact, encode_ns, encode_peak = _measure_peak(
        lambda: encode_pipeline(source, [stage])
    )
    reconstructed, decode_ns, decode_peak = _measure_peak(
        lambda: decode_pipeline(artifact, max_output_bytes=max(len(source), 1))
    )

    return {
        "workload": name,
        "codec": codec,
        "source_bytes": len(source),
        "encoded_payload_bytes": len(artifact.payload),
        "payload_ratio": round(len(artifact.payload) / max(len(source), 1), 6),
        "encode_time_ns": encode_ns,
        "decode_time_ns": decode_ns,
        "encode_peak_traced_bytes": encode_peak,
        "decode_peak_traced_bytes": decode_peak,
        "roundtrip_exact": reconstructed == source,
        "scope": "single-process payload-only measurement; excludes serialized capsule, indexes, dictionaries, transfer, coordination, replication, and recovery",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--size", type=int, default=262_144, help="approximate bytes per generated workload")
    parser.add_argument("--seed", type=int, default=931, help="deterministic random workload seed")
    args = parser.parse_args()

    workloads = build_workloads(size=args.size, seed=args.seed)
    results = [
        benchmark_one(name, payload, codec)
        for name, payload in workloads.items()
        for codec in ("identity", "zlib")
    ]
    report = {
        "benchmark_version": "0.1.0",
        "python": sys.version,
        "platform": platform.platform(),
        "seed": args.seed,
        "requested_workload_size_bytes": args.size,
        "method": "one local encode and decode sample per workload/codec; use repeated runs for publishable performance conclusions",
        "results": results,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if all(item["roundtrip_exact"] for item in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
