import iuliia
from iuliia.schema import TranslitSchema


def test_translate():
    schema = TranslitSchema(name="test", mapping={})
    assert schema.translate("Iuliia") == "Iuliia"

    # deprecated
    assert iuliia.translate("Iuliia", schema) == "Iuliia"


def test_mapping():
    schema = TranslitSchema(name="test", mapping={"a": "1", "i": "2", "l": "3", "u": "4"})
    assert schema.translate("Iuliia") == "243221"


def test_prev_mapping():
    schema = TranslitSchema(name="test", mapping={}, prev_mapping={"li": ""})
    assert schema.translate("Iuliia") == "Iulia"


def test_next_mapping():
    schema = TranslitSchema(name="test", mapping={}, next_mapping={"iu": "y"})
    assert schema.translate("Iuliia") == "Yuliia"


def test_ending_mapping():
    schema = TranslitSchema(name="test", mapping={}, ending_mapping={"ia": "ya"})
    assert schema.translate("Iuliia") == "Iuliya"


def test_short_word():
    schema = TranslitSchema(name="test", mapping={})
    assert schema.translate("Iu") == "Iu"


def test_empty_word():
    schema = TranslitSchema(name="test", mapping={})
    assert schema.translate("") == ""
