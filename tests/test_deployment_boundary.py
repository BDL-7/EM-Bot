import json
from pathlib import Path


HOST_ROOT = Path(__file__).parents[1] / "host_app"


def test_host_directory_contains_only_runtime_material():
    runtime_files = {
        path.relative_to(HOST_ROOT).as_posix()
        for path in HOST_ROOT.rglob("*")
        if path.is_file()
        and path.name != "manifest.json"
        and "__pycache__" not in path.parts
    }
    assert runtime_files == {
        ".python-version",
        "__init__.py",
        "app.py",
        "requirements.txt",
        "static/microbot.js",
        "static/styles.css",
        "templates/index.html",
    }


def test_host_directory_excludes_private_project_artifacts():
    bundled_names = [path.name.lower() for path in HOST_ROOT.rglob("*") if path.is_file()]
    assert not any(name.endswith((".pdf", ".docx", ".env")) for name in bundled_names)
    assert "pilot_source_register.md" not in bundled_names
    assert "phase_0_pilot_boundary.md" not in bundled_names
    assert "phase_2_baas_configuration.md" not in bundled_names


def test_committed_manifest_describes_only_the_isolated_host():
    manifest_path = HOST_ROOT / "manifest.json"
    assert manifest_path.is_file()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["metadata"]["appmode"] == "python-api"
    assert manifest["metadata"]["entrypoint"] == "app:app"
    assert manifest["environment"]["python"]["requires"] == ">=3.10,<3.14"
    files = set(manifest["files"])
    assert "app.py" in files
    assert "templates/index.html" in files
    assert "static/microbot.js" in files
    assert not any(path.lower().endswith((".pdf", ".docx", ".env")) for path in files)
