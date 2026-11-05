import pytest

from adaptive_swarm_compression import (
    PipelineStage,
    decode_pipeline,
    encode_pipeline,
    list_codecs,
)


def test_identity_roundtrip():
    source = b"swarm information" * 100
    artifact = encode_pipeline(source, [PipelineStage("identity", "1", {})])
    assert decode_pipeline(artifact) == source


def test_zlib_roundtrip():
    source = (b"repeated structured data\x00" * 1000) + bytes(range(256))
    import zlib

    artifact = encode_pipeline(
        source,
        [PipelineStage("zlib", zlib.ZLIB_VERSION, {"level": 6})],
    )
    assert decode_pipeline(artifact) == source
    assert len(artifact.payload) < len(source)


def test_pipeline_order_roundtrip():
    source = b"abcabcabc" * 200
    import zlib

    stages = [
        PipelineStage("identity", "1", {}),
        PipelineStage("zlib", zlib.ZLIB_VERSION, {"level": 9}),
    ]
    assert decode_pipeline(encode_pipeline(source, stages)) == source


def test_integrity_metadata_is_enforced():
    source = b"integrity"
    artifact = encode_pipeline(source, [])
    altered = type(artifact)(
        payload=artifact.payload,
        stages=artifact.stages,
        source_sha256="0" * 64,
        source_size=artifact.source_size,
    )
    with pytest.raises(ValueError, match="digest"):
        decode_pipeline(altered)


def test_output_limit_is_enforced():
    artifact = encode_pipeline(b"x" * 1000, [])
    with pytest.raises(ValueError, match="exceeds"):
        decode_pipeline(artifact, max_output_bytes=10)


def test_codec_registry_is_explicit():
    assert {item["name"] for item in list_codecs()} >= {"identity", "zlib"}
