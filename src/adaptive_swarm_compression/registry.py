"""Small explicit registry of trusted local codecs."""

from dataclasses import dataclass
import zlib
from typing import Callable


@dataclass(frozen=True)
class Codec:
    name: str
    version: str
    encode: Callable[[bytes, dict], bytes]
    decode: Callable[[bytes, dict], bytes]
    guarantee: str = "exact"


_CODECS: dict[str, Codec] = {}


def register_codec(codec: Codec) -> None:
    """Register a codec. Re-registering a name replaces its implementation."""
    if not codec.name or not codec.version:
        raise ValueError("codec name and version are required")
    if codec.guarantee != "exact":
        raise ValueError("the initial pipeline supports exact codecs only")
    _CODECS[codec.name] = codec


def get_codec(name: str) -> Codec:
    try:
        return _CODECS[name]
    except KeyError as exc:
        raise ValueError(f"unknown codec: {name}") from exc


def list_codecs() -> list[dict[str, str]]:
    return [
        {"name": item.name, "version": item.version, "guarantee": item.guarantee}
        for item in sorted(_CODECS.values(), key=lambda value: value.name)
    ]


def _identity_encode(data: bytes, parameters: dict) -> bytes:
    return data


def _identity_decode(data: bytes, parameters: dict) -> bytes:
    return data


def _zlib_encode(data: bytes, parameters: dict) -> bytes:
    level = int(parameters.get("level", 6))
    if not 0 <= level <= 9:
        raise ValueError("zlib level must be between 0 and 9")
    return zlib.compress(data, level)


def _zlib_decode(data: bytes, parameters: dict) -> bytes:
    limit = int(parameters.get("_max_output_bytes", 64 * 1024 * 1024))
    if limit < 0:
        raise ValueError("max output size must be non-negative")
    decoder = zlib.decompressobj()
    output = decoder.decompress(data, limit + 1)
    if len(output) > limit or decoder.unconsumed_tail:
        raise ValueError("decoded output exceeds max_output_bytes")
    output += decoder.flush()
    if len(output) > limit:
        raise ValueError("decoded output exceeds max_output_bytes")
    if not decoder.eof or decoder.unused_data or decoder.unconsumed_tail:
        raise ValueError("invalid or trailing zlib stream data")
    return output


register_codec(Codec("identity", "1", _identity_encode, _identity_decode))
register_codec(Codec("zlib", "rfc1950-1", _zlib_encode, _zlib_decode))
