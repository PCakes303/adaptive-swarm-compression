import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(relative_path):
    return json.loads((ROOT / relative_path).read_text(encoding="utf-8"))


def test_repository_metadata_documents_are_valid_json():
    for path in (
        "manifest.json",
        "capabilities.json",
        "compatibility.json",
        "schemas/representation-capsule.schema.json",
    ):
        assert isinstance(load_json(path), dict)


def test_manifest_capabilities_and_compatibility_align():
    manifest = load_json("manifest.json")
    capabilities = load_json("capabilities.json")
    compatibility = load_json("compatibility.json")

    assert manifest["id"] == "adaptive-swarm-compression"
    assert manifest["visibility"] == "public"
    assert manifest["maturity"] == "experimental"
    assert manifest["license"]["expression"] == "Apache-2.0"
    assert manifest["license"]["status"] == "selected"
    assert capabilities["repository_id"] == manifest["id"]
    assert compatibility["repository"] == manifest["id"]

    manifest_dependencies = {item["id"] for item in manifest["dependencies"]}
    compatibility_dependencies = {
        item["repository_id"] for item in compatibility["dependencies"]
    }
    assert manifest_dependencies == compatibility_dependencies
    assert all(item["status"] == "declared" for item in compatibility["dependencies"])
    assert compatibility["tested_combinations"] == []


def test_capability_evidence_paths_exist():
    capabilities = load_json("capabilities.json")
    for capability in capabilities["capabilities"]:
        for evidence_path in capability["evidence"]:
            assert (ROOT / evidence_path).is_file(), evidence_path


def test_private_research_is_not_a_public_dependency():
    manifest = load_json("manifest.json")
    compatibility = load_json("compatibility.json")
    all_dependencies = {
        item["id"] for item in manifest["dependencies"]
    } | {
        item["repository_id"] for item in compatibility["dependencies"]
    }
    assert "swarm-information-research" not in all_dependencies
