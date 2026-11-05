"""Experimental primitives for adaptive swarm compression."""

from .models import EncodedArtifact, PipelineStage
from .pipeline import decode_pipeline, encode_pipeline
from .registry import get_codec, list_codecs, register_codec

__all__ = [
    "EncodedArtifact",
    "PipelineStage",
    "decode_pipeline",
    "encode_pipeline",
    "get_codec",
    "list_codecs",
    "register_codec",
]

__version__ = "0.1.0"
