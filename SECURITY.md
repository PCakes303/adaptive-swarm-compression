# Security Policy

## Scope

This project processes potentially untrusted byte streams and will eventually explore distributed representations and shared dependencies. Decoder safety, resource exhaustion, integrity, authorization, and cross-agent isolation are in scope.

## Reporting

Do not publish exploit details for an unpatched vulnerability. Use GitHub's private vulnerability reporting feature if enabled for this repository. If it is unavailable, contact the maintainer through a private channel before public disclosure.

## Current safeguards and limitations

- The initial package is experimental and must not be exposed as a network service.
- Treat all encoded payloads and capsule metadata as untrusted.
- Apply input-size, memory, CPU, and decompression-expansion limits in any service wrapper.
- Verify integrity before accepting reconstructed output.
- Do not load arbitrary codecs or plugins from untrusted sources.
- Do not share dictionaries or learned models across trust boundaries without leakage analysis.
- Hashes alone do not establish authenticity; use authenticated provenance and signatures where required.

## Future requirements

Before distributed deployment: threat model, identity and authorization, tenant isolation, key management, replay protection, dependency pinning, signed artifacts, audit trail, revocation, quotas, and recovery tests.

## Supported versions

No production-supported release has been declared. Security fixes and compatibility guarantees will be documented when release policy is established.
