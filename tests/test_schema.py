import iuliia


def test_init():
    schema = iuliia.Schema(name="test", mapping={"a": "z"})
    assert schema.name == "test"
    assert schema.map.map == {"a": "z", "A": "Z"}


def test_str():
    schema = iuliia.Schema(name="test", mapping={})
    assert str(schema) == "test"
    assert repr(schema) == "test"
