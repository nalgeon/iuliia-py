from iuliia import engine


def test_translate():
    schema = engine.Schema({})
    assert engine.translate("Iuliia", schema) == "Iuliia"


def test_mapping():
    schema = engine.Schema({"a": "1", "i": "2", "l": "3", "u": "4"})
    assert engine.translate("Iuliia", schema) == "243221"


def test_prev_mapping():
    schema = engine.Schema({}, prev_mapping={"li": ""})
    assert engine.translate("Iuliia", schema) == "Iulia"


def test_next_mapping():
    schema = engine.Schema({}, next_mapping={"iu": "y"})
    assert engine.translate("Iuliia", schema) == "Yuliia"


def test_ending_mapping():
    schema = engine.Schema({}, ending_mapping={"ia": "ya"})
    assert engine.translate("Iuliia", schema) == "Iuliya"


def test_short_word():
    schema = engine.Schema({})
    assert engine.translate("Iu", schema) == "Iu"


def test_empty_word():
    schema = engine.Schema({})
    assert engine.translate("", schema) == ""
