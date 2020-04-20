import pytest
from iuliia.schema import Mapping


@pytest.fixture
def mapping():
    return Mapping({"a": "x", "b": "y", "cd": "zz"})


def test_map(mapping):
    assert mapping.map == {"a": "x", "b": "y", "cd": "zz", "A": "X", "B": "Y", "Cd": "Zz"}


def test_get(mapping):
    assert mapping.get("a") == "x"
    assert mapping.get("B") == "Y"
    assert mapping.get("f") is None
    assert mapping.get("g", "g") == "g"


def test_str(mapping):
    assert str(mapping) == str(mapping.map)
    assert repr(mapping) == repr(mapping.map)
