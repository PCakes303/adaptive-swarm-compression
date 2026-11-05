# Ecosystem Integration Boundaries

## Purpose

This document maps the public compression implementation to existing Agent Intelligence Ecosystem components. These are declared relationships, not tested runtime integrations.

## Declared dependencies

| Repository | Intended relationship | Current status |
|---|---|---|
| `aix-codecs` | Reuse compatible serialization and codec abstractions | Declared; no adapter or conformance test |
| `aix-core` | Representation negotiation and capability semantics | Declared; no protocol mapping |
| `agent-resource-manifest` | Resource and representation metadata conventions | Declared; repository manifest uses master schema |
| `swarm-state-mesh` | Future shared references, state, and recovery metadata | Declared; no runtime integration |
| `swarm-runtime` | Future distributed execution and scheduling | Declared; no runtime integration |
| `intelligence-knowledge-graph` | Future graph-aware representation experiments | Declared; no graph adapter |
| `agent-audit-provenance` | Future transformation lineage and evidence records | Declared; no event integration |

## Separation of responsibilities

- This repository owns local codec pipeline implementation and compression-specific experiments.
- AIX owns message and representation negotiation semantics; this project does not define a competing agent protocol.
- Swarm Runtime and State Mesh own distributed execution and shared-state behavior; this project does not implement those systems.
- Resource Manifest and Schema Registry own shared resource/schema governance; this project references their contracts.
- Audit & Provenance owns ecosystem audit event contracts; this project must emit compatible transformation records if that integration is later implemented.

## Compatibility policy

All dependencies remain `declared` in `compatibility.json`. A relationship may be promoted to `tested` only after a pinned version combination, reproducible fixture, automated test, and evidence reference are committed.

## Promotion gates

1. Pin the relevant upstream contract version.
2. Add a fixture or adapter that uses the actual upstream contract.
3. Test positive and negative cases.
4. Verify exactness, authorization, provenance, and failure behavior.
5. Publish test evidence and update compatibility metadata.
