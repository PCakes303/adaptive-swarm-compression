from benchmarks.workloads import build_workloads


def test_workloads_are_deterministic():
    first = build_workloads(size=4096, seed=17)
    second = build_workloads(size=4096, seed=17)
    assert first == second
    assert set(first) == {
        "repetitive_text",
        "structured_records",
        "numeric_series",
        "deterministic_random_bytes",
    }


def test_random_workload_changes_with_seed():
    first = build_workloads(size=1024, seed=1)
    second = build_workloads(size=1024, seed=2)
    assert first["deterministic_random_bytes"] != second["deterministic_random_bytes"]


def test_benchmark_harness_checks_exact_reconstruction():
    from benchmarks.run import benchmark_one

    result = benchmark_one("small-repetitive", b"swarm-state" * 100, "zlib")
    assert result["roundtrip_exact"] is True
    assert result["encoded_payload_bytes"] < result["source_bytes"]
