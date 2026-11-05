# Baseline Benchmark Harness

Run from the repository root:

```bash
python -m pip install -e ".[dev]"
python -m benchmarks.run --size 262144 --seed 931
```

The command emits JSON for deterministic repetitive text, structured records, numeric-series bytes, and seeded random bytes. It compares the local identity and zlib codec stages.

Each result reports source and encoded payload bytes, payload ratio, one encode/decode duration, traced peak memory, and exact round-trip status.

## Measurement boundary

This first harness is intentionally narrow. It measures one process and one sample per workload/codec. It excludes serialized capsule metadata, indexes, dictionaries, model storage, network transfer, coordination, replication, cache effects, and recovery. It must not be used to claim swarm-level improvement or robust performance superiority.

Use repeated runs, fixed environments, confidence/dispersion reporting, and expanded accounting before publishing performance conclusions.
