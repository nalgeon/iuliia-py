import os
import timeit
import pytest
from iuliia import engine
from iuliia.schema import Schema


def test_translate():
    schema = Schema(name="test", mapping={})
    assert engine.translate("Iuliia", schema) == "Iuliia"


def test_mapping():
    schema = Schema(name="test", mapping={"a": "1", "i": "2", "l": "3", "u": "4"})
    assert engine.translate("Iuliia", schema) == "243221"


def test_prev_mapping():
    schema = Schema(name="test", mapping={}, prev_mapping={"li": ""})
    assert engine.translate("Iuliia", schema) == "Iulia"


def test_next_mapping():
    schema = Schema(name="test", mapping={}, next_mapping={"iu": "y"})
    assert engine.translate("Iuliia", schema) == "Yuliia"


def test_ending_mapping():
    schema = Schema(name="test", mapping={}, ending_mapping={"ia": "ya"})
    assert engine.translate("Iuliia", schema) == "Iuliya"


def test_short_word():
    schema = Schema(name="test", mapping={})
    assert engine.translate("Iu", schema) == "Iu"


def test_empty_word():
    schema = Schema(name="test", mapping={})
    assert engine.translate("", schema) == ""


@pytest.mark.skipif(
    os.getenv("TEST_TIMING") is None, reason="skip timing test until explicitly requested"
)
def test_timing():
    mapping = {chr(i): chr(i) for i in range(ord("a"), ord("z"))}
    schema = Schema(name="test", mapping=mapping)
    source = "The quick brown fox jumps over the lazy dog"
    elapsed_sec = timeit.timeit(lambda: engine.translate(source, schema), number=10000)
    max_sec = 1.0
    assert elapsed_sec < max_sec
