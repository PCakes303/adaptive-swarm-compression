"""Deterministic lossless pipeline execution with source integrity checking."""

from hashlib import sha256
from collections.abc import Iterable

from .models import EncodedArtifact, PipelineStage
from .registry import get_codec


def encode_pipeline(data: bytes, stages: Iterable[PipelineStage]) -> EncodedArtifact:
    if not isinstance(data, bytes):
        raise TypeError("data must be bytes")
    ordered = tuple(stages)
    payload = data
    for stage in ordered:
        codec = get_codec(stage.codec)
        if stage.version != codec.version:
            raise ValueError(
                f"codec version mismatch for {stage.codec}: "
                f"artifact requests {stage.version}, installed {codec.version}"
            )
        payload = codec.encode(payload, stage.parameters)
    return EncodedArtifact(
        payload=payload,
        stages=ordered,
        source_sha256=sha256(data).hexdigest(),
        source_size=len(data),
    )


def decode_pipeline(artifact: EncodedArtifact, *, max_output_bytes: int = 64 * 1024 * 1024) -> bytes:
    if artifact.guarantee != "exact":
        raise ValueError("this decoder accepts exact artifacts only")
    if max_output_bytes < 0:
        raise ValueError("max_output_bytes must be non-negative")
    payload = artifact.payload
    for stage in reversed(artifact.stages):
        codec = get_codec(stage.codec)
        if stage.version != codec.version:
            raise ValueError(
                f"codec version mismatch for {stage.codec}: "
                f"artifact requests {stage.version}, installed {codec.version}"
            )
        payload = codec.decode(payload, stage.parameters)
        if len(payload) > max_output_bytes:
            raise ValueError("decoded output exceeds max_output_bytes")
    if len(payload) != artifact.source_size:
        raise ValueError("reconstructed size does not match artifact metadata")
    if sha256(payload).hexdigest() != artifact.source_sha256:
        raise ValueError("reconstructed content digest does not match")
    return payload
