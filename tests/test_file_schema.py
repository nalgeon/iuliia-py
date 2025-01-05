import pytest
from iuliia.repo import FileSchema, SCHEMA_DIR

SCHEMA_PATH = SCHEMA_DIR / "wikipedia.json"


def test_name():
    schema = FileSchema("wikipedia", SCHEMA_PATH)
    assert schema.name == "wikipedia"
    assert schema._schema is None


def test_invalid_name():
    with pytest.raises(ValueError) as exc:
        schema = FileSchema("wikipedia", "./wikipedia.json")
        schema.translate("wikipedia")
    assert str(exc.value).startswith("Schema path does not exist:")


def test_description():
    schema = FileSchema("wikipedia", SCHEMA_PATH)
    assert schema.description == "Wikipedia transliteration schema"
    assert schema.translate("wikipedia") == "wikipedia"
    assert schema._schema is not None


def test_samples():
    schema = FileSchema("wikipedia", SCHEMA_PATH)
    assert len(schema.samples) > 0
    assert schema._schema is not None


def test_translate():
    schema = FileSchema("wikipedia", SCHEMA_PATH)
    assert schema.translate("wikipedia") == "wikipedia"
    assert schema._schema is not None


def test_str():
    schema = FileSchema("wikipedia", SCHEMA_PATH)
    assert str(schema) == "wikipedia"
    assert repr(schema) == "FileSchema('wikipedia')"
