"""Deterministic synthetic workloads for first-pass codec comparisons."""

import json
import random
import struct


def _repeat_to_size(pattern: bytes, size: int) -> bytes:
    return (pattern * ((size + len(pattern) - 1) // len(pattern)))[:size]


def build_workloads(size: int = 262_144, seed: int = 931) -> dict[str, bytes]:
    """Return reproducible workloads; size is an approximate target per workload."""
    if size <= 0:
        raise ValueError("size must be positive")

    repetitive = _repeat_to_size(b"agent-state|capability|evidence|provenance\n", size)

    count = max(1, size // 96)
    records = [
        {
            "agent": f"agent-{index % 64:02d}",
            "sequence": index,
            "kind": ("observation", "heartbeat", "evidence")[index % 3],
            "capabilities": ["parse", "verify", "index"] if index % 4 else ["verify"],
            "payload": f"record-{index % 128:03d}",
        }
        for index in range(count)
    ]
    structured = json.dumps(records, separators=(",", ":"), sort_keys=True).encode("utf-8")

    numeric_count = max(1, size // 4)
    numeric = b"".join(
        struct.pack("<I", (index // 8) % 4096)
        for index in range(numeric_count)
    )

    generator = random.Random(seed)
    random_bytes = generator.randbytes(size)

    return {
        "repetitive_text": repetitive,
        "structured_records": structured,
        "numeric_series": numeric,
        "deterministic_random_bytes": random_bytes,
    }
