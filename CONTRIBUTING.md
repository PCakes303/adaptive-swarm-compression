# Contributing

## Current stage

The project is experimental. Contributions should favor small, testable changes and reproducible evidence over speculative claims.

## Before proposing a change

- Read README.md, ARCHITECTURE.md, and SECURITY.md.
- Identify whether the change is lossless, bounded-loss, approximate, or semantic.
- State codec and dependency versions.
- Include a baseline and measurable hypothesis for performance changes.
- Preserve exact source evidence where required.

## Code expectations

- Type hints for public Python interfaces.
- Deterministic tests where possible.
- Byte-for-byte round-trip tests for lossless transformations.
- Explicit error handling for malformed data and unsupported versions.
- No hidden network access or arbitrary plugin execution.
- Document resource limits and worst-case behavior.

## Benchmark expectations

Report full accounting boundaries, including metadata and shared dependencies. Include negative results and avoid comparing different input workloads.

## Pull requests

Keep pull requests focused. Explain behavior, compatibility impact, test coverage, security implications, and benchmark evidence. Do not describe planned functionality as implemented.
