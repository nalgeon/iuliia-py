import pytest
from iuliia.mapping import Mapping, LetterMapping, PrevMapping, NextMapping, EndingMapping


@pytest.fixture
def mapping():
    return Mapping({"a": "x", "b": "yy"})


def test_map(mapping):
    assert mapping.map == {"a": "x", "b": "yy"}


def test_get(mapping):
    assert mapping.get("a") == "x"
    assert mapping.get("b") == "yy"
    assert mapping.get("c") is None
    assert mapping.get("d", "d") == "d"


def test_str(mapping):
    assert str(mapping) == str(mapping.map)
    assert repr(mapping) == repr(mapping.map)


def test_letter_mapping():
    mapping = LetterMapping({"a": "x", "b": "yy"})
    assert mapping.map == {"a": "x", "A": "X", "b": "yy", "B": "Yy"}


def test_prev_mapping():
    mapping = PrevMapping({"ax": "xx", "bx": "xxx"})
    assert mapping.map == {
        "ax": "xx",
        "Ax": "xx",
        "AX": "Xx",
        "bx": "xxx",
        "Bx": "xxx",
        "BX": "Xxx",
    }


def test_next_mapping():
    mapping = NextMapping({"xa": "xx", "xb": "xxx"})
    assert mapping.map == {
        "xa": "xx",
        "Xa": "Xx",
        "XA": "Xx",
        "xb": "xxx",
        "Xb": "Xxx",
        "XB": "Xxx",
    }


def test_ending_mapping():
    mapping = EndingMapping({"aa": "xx", "bb": "yy"})
    assert mapping.map == {"aa": "xx", "AA": "XX", "bb": "yy", "BB": "YY"}
