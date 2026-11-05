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
