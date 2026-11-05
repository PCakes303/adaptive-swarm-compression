# Roadmap

## 0.1 — Local foundation
- [x] Establish project scope and technical boundaries.
- [x] Define stable codec interface (local exact-codec contract).
- [x] Implement identity and zlib lossless codecs.
- [x] Implement pipeline encode/decode with integrity verification.
- [x] Add round-trip, integrity, malformed-stream, and output-limit tests.
- [x] Add deterministic local baseline benchmark command (narrow measurement boundary; CI confirmation pending).
- [x] Add repository manifest, capability declarations, compatibility metadata, agent instructions, and machine-readable discovery index.
- [x] Add local metadata-consistency regression tests; master schema validation and CI confirmation remain pending.

## 0.2 — Representation contracts
- Add versioned representation capsule validation.
- Record codec versions, parameters, dependencies, exactness, and provenance.
- Add compatibility checks and explicit resource limits.

## 0.3 — Workload-aware composition
- Add data characterization features.
- Add bounded candidate selection and cost estimates.
- Compare planner decisions with fixed baseline policies.

## 0.4 — Structured and selective data
- Add chunked representations and range reconstruction.
- Evaluate event delta and graph-aware representations.
- Verify selective results against full reconstruction.

## 0.5 — Collective strategies
- Prototype shared dictionaries and content-addressed deduplication.
- Include synchronization, storage, and recovery costs.
- Evaluate multi-agent workloads in a reproducible simulator.

## 0.6 — Swarm integration
- Define transport-neutral coordination interfaces.
- Reuse suitable AIX and ecosystem contracts.
- Add resilience, trust, authorization, and provenance controls.

Milestones are targets, not claims of completed functionality. Each feature requires tests and documented evidence before being marked supported.
