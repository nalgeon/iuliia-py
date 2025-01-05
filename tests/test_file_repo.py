from pathlib import Path
import pytest
from iuliia.repo import FileRepo


def test_init():
    repo = FileRepo()
    assert repo.base_dir == Path(__file__).parent.parent / "iuliia" / "schemas"
    assert len(repo.schemas) > 0


def test_has():
    repo = FileRepo()
    assert repo.has("wikipedia")
    assert not repo.has("unknown")


def test_get():
    repo = FileRepo()
    schema = repo.get("wikipedia")
    assert schema.name == "wikipedia"
    assert schema.translate("wikipedia") == "wikipedia"


def test_get_invalid():
    repo = FileRepo()
    with pytest.raises(ValueError) as exc:
        repo.get("unknown")
    assert str(exc.value).startswith("Schema not found: unknown")


def test_names():
    repo = FileRepo()
    assert len(repo.names()) > 0
    assert "wikipedia" in repo.names()
    assert "unknown" not in repo.names()


def test_items():
    repo = FileRepo()
    assert len(repo.items()) > 0
    assert any(name == "wikipedia" for name, _ in repo.items())
    assert any(schema.name == "wikipedia" for _, schema in repo.items())
    assert not any(name == "unknown" for name, _ in repo.items())
    assert not any(schema.name == "unknown" for _, schema in repo.items())
