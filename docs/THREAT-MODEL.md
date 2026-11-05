# Threat Model

## Scope

The current implementation is a local Python library and benchmark harness. It does not expose a network service, collect external data, execute agent workloads, or authenticate remote peers. This threat model covers current local inputs and the risks introduced by planned representation sharing.

## Assets

- Authoritative source bytes and source digests
- Encoded payloads and representation metadata
- Codec implementations and version identifiers
- Future dictionaries, indexes, models, and content references
- Benchmark inputs and results
- Provenance and authorization metadata

## Trust boundaries

- Callers provide source bytes and pipeline metadata.
- Encoded payloads and capsules may be malformed or adversarial.
- Codec implementations are trusted code; arbitrary plugins are not supported.
- Future shared dictionaries and models may cross tenant or administrative boundaries.
- Ecosystem dependencies are declarations until compatibility tests establish otherwise.

## Threats and mitigations

| Threat | Current or required mitigation |
|---|---|
| Decompression bomb / resource exhaustion | Bounded output size; test malformed streams; future CPU, wall-time, nesting, and aggregate-memory budgets |
| Malformed or trailing compressed data | Strict stream completion and trailing-data checks |
| Payload or metadata tampering | Source-size and SHA-256 reconstruction verification; authenticated provenance remains future work |
| Codec/version confusion | Stable wire-format identifiers and explicit version checks |
| Malicious codec plugin | No arbitrary plugin loading; only explicitly registered local codecs |
| Cross-tenant dictionary leakage | No shared dictionary service exists; future sharing requires isolation and leakage analysis |
| Poisoned shared model or index | No shared model/index service exists; future artifacts require provenance, validation, and trust policy |
| Stale or dangling content references | No distributed reference system exists; future references require immutable identity, versioning, expiry, and recovery semantics |
| Privacy leakage through metadata | Capsules must avoid secrets and unnecessary personal data; authorization is external to the capsule |
| False confidence in benchmark results | Narrow measurement boundary and one-sample limitations are stated in every report |

## Security invariants

1. A digest proves byte equality against a known digest; it does not prove source authenticity or authorization.
2. Discoverability does not grant access.
3. Lossy and semantic representations must never replace exact evidence silently.
4. Missing dependencies, unknown versions, or failed integrity checks must fail closed.
5. Every decoder must have explicit resource limits.
6. Shared dictionaries, indexes, and models must be scoped to trust domains and include synchronization/recovery costs.
7. No private research material or credentials may enter public artifacts.

## Residual risks

The initial local implementation is experimental. Resource limits are not yet a complete CPU or memory sandbox. The benchmark harness is not a security test. No independent security review has occurred. Do not expose the library through an untrusted network service.
