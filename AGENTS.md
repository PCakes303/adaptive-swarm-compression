# Agent Instructions

## Mission

Build a reproducible, security-conscious research implementation for adaptive and collective information representation. Optimize total useful-information cost, not isolated compression ratio.

## Required reading

Before changing behavior, read:
- README.md
- ARCHITECTURE.md
- ROADMAP.md
- SECURITY.md
- docs/THREAT-MODEL.md
- manifest.json
- capabilities.json
- compatibility.json

## Non-negotiable rules

1. Never claim arbitrary incompressible data can be losslessly compressed to an arbitrarily small fixed size.
2. Keep exact, bounded-loss, approximate, and semantic representations distinct.
3. Never silently replace authoritative source evidence with a lossy or semantic representation.
4. Include metadata, indexes, dictionaries, models, transfer, coordination, replication, verification, and recovery in system-level cost accounting.
5. Do not claim distributed swarm behavior, shared-dictionary exchange, selective reconstruction, or adaptive compilation until implemented and tested.
6. Do not mark an integration dependency as tested without reproducible cross-repository evidence.
7. Keep this public repository independently buildable. Do not require or expose restricted research material.
8. Treat payloads, manifests, and representation capsules as untrusted input.
9. Bound CPU, memory, decompression output, nesting, and input sizes at trust boundaries.
10. Do not load arbitrary codec plugins or execute untrusted repository code.

## Development workflow

- Python 3.10+.
- Use type hints for public interfaces.
- Add deterministic tests for every behavior change.
- Lossless transformations require byte-for-byte round-trip tests.
- Decoder changes require malformed-input and resource-limit tests.
- Metadata changes must preserve manifest/capability/compatibility consistency.
- Benchmark claims require repeatable runs, declared hardware/software, full accounting boundaries, and negative results.
- Run `python -m pytest -q` before proposing a change.
- Run `python -m benchmarks.run --size 262144 --seed 931` when changing codec or benchmark behavior.

## Status language

Use `planned`, `scaffolded`, `experimental`, `tested`, or `stable` only when the repository's evidence supports that status. Source code existing is not proof that tests passed. CI passing is not proof of production readiness.

## Integration

The master ecosystem registry is authoritative for repository IDs and declared dependencies. This repository's compatibility file must keep dependencies at `declared` until pinned cross-repository tests exist.
