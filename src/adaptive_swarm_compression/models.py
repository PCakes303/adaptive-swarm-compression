"""Typed data models for local lossless pipeline execution."""

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class PipelineStage:
    """A named codec stage and its JSON-compatible parameters."""

    codec: str
    version: str
    parameters: dict[str, Any]


@dataclass(frozen=True)
class EncodedArtifact:
    """Encoded bytes plus the ordered inverse operations and source digest."""

    payload: bytes
    stages: tuple[PipelineStage, ...]
    source_sha256: str
    source_size: int
    guarantee: str = "exact"
    artifact_version: str = "0.1.0"
