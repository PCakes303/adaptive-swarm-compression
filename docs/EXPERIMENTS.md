# Experiments

## EXP-001 — Local codec baselines
**Status:** Initial harness planned.

Compare identity and zlib on repetitive, structured, numeric-like, and random byte workloads. Verify exact reconstruction and record time, memory, and encoded size.

## EXP-002 — Independent versus shared dictionaries
**Status:** Planned.

Compare per-agent compression with a shared dictionary strategy. Count dictionary storage, distribution, update, synchronization, and recovery overhead.

## EXP-003 — Representation pipeline selection
**Status:** Planned.

Compare a fixed codec policy with a bounded planner over known codec capabilities. Count planner time and all dependencies.

## EXP-004 — Selective reconstruction
**Status:** Planned.

Evaluate chunked representations and indexed range access against full reconstruction, including index and metadata overhead.
