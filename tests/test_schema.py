import iuliia


def test_init():
    schema = iuliia.Schema("test", {"a": "z"})
    assert schema.name == "test"
    assert schema.map.map == {"a": "z", "A": "Z"}


def test_str():
    schema = iuliia.Schema("test", {})
    assert str(schema) == "test"
    assert repr(schema) == "test"
