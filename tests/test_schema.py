from iuliia.schema import TranslitSchema


def test_init():
    schema = TranslitSchema(
        name="test", mapping={"a": "z"}, description="test schema", samples=[["aaa", "zzz"]]
    )
    assert schema.name == "test"
    assert schema.description == "test schema"
    assert schema.samples == [["aaa", "zzz"]]
    assert schema.map == {"a": "z", "A": "Z"}


def test_mapping():
    schema = TranslitSchema(name="test", mapping={"a": "x", "b": "yy"})
    assert schema.map == {"a": "x", "A": "X", "b": "yy", "B": "Yy"}


def test_prev_mapping():
    schema = TranslitSchema(name="test", mapping={}, prev_mapping={"ax": "xx", "bx": "xxx"})
    assert schema.prev_map == {
        "ax": "xx",
        "Ax": "xx",
        "AX": "Xx",
        "bx": "xxx",
        "Bx": "xxx",
        "BX": "Xxx",
    }


def test_next_mapping():
    schema = TranslitSchema(name="test", mapping={}, next_mapping={"xa": "xx", "xb": "xxx"})
    assert schema.next_map == {
        "xa": "xx",
        "Xa": "Xx",
        "XA": "Xx",
        "xb": "xxx",
        "Xb": "Xxx",
        "XB": "Xxx",
    }


def test_ending_mapping():
    schema = TranslitSchema(name="test", mapping={}, ending_mapping={"aa": "xx", "bb": "yy"})
    assert schema.ending_map == {"aa": "xx", "AA": "XX", "bb": "yy", "BB": "YY"}


def test_str():
    schema = TranslitSchema(name="test", mapping={})
    assert str(schema) == "test"
    assert repr(schema) == "TranslitSchema('test')"
