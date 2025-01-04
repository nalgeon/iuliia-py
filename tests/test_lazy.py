import pytest
from iuliia.lazy import LazySchema


def test_name():
    schema = LazySchema(name="wikipedia")
    assert schema.name == "wikipedia"
    assert schema._schema is None


def test_invalid_name():
    with pytest.raises(ValueError) as exc:
        schema = LazySchema(name="invalid")
        schema.translate("wikipedia")
    assert str(exc.value).startswith("Schema path does not exist:")


def test_description():
    schema = LazySchema(name="wikipedia")
    assert schema.description == "Wikipedia transliteration schema"
    assert schema.translate("wikipedia") == "wikipedia"
    assert schema._schema is not None


def test_samples():
    schema = LazySchema(name="wikipedia")
    assert len(schema.samples) > 0
    assert schema._schema is not None


def test_translate():
    schema = LazySchema(name="wikipedia")
    assert schema.translate("wikipedia") == "wikipedia"
    assert schema._schema is not None


def test_str():
    schema = LazySchema(name="test")
    assert str(schema) == "test"
    assert repr(schema) == "LazySchema('test')"
