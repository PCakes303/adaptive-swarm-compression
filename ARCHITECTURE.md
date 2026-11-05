# Architecture

## Current implementation boundary

The initial package is a local, deterministic foundation for describing and executing lossless codec pipelines. It is not yet a distributed swarm runtime, shared-dictionary service, representation compiler, or production storage system.

## Core concepts

- **Codec:** a named, versioned encoder/decoder pair with a declared guarantee.
- **Pipeline:** an ordered sequence of codecs. Each stage consumes the previous stage's output.
- **EncodedArtifact:** payload plus metadata needed to decode it.
- **Representation capsule:** a portable description of format, stages, exactness, dependencies, and integrity.
- **Benchmark:** measures payload and operational costs against a baseline.

## Planned evolution

1. Local codec interfaces and exact round-trip tests.
2. Reproducible benchmark harness.
3. Typed transformation stages and representation capsule validation.
4. Constrained pipeline planner.
5. Chunking and selective reconstruction.
6. Shared dictionaries and content-addressed references.
7. Swarm placement, coordination, and fault recovery.

## Design constraints

- Lossless and lossy operations are different types, not flags that can be ignored.
- Decoder dependencies and versions are explicit.
- Resource limits are required before accepting untrusted payloads.
- Hashes validate bytes; they do not prove authorization or provenance by themselves.
- Distributed behavior is added only with explicit consistency and failure semantics.
