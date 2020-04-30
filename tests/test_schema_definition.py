import pytest
from iuliia.schema import SchemaDefinition


def test_init():
    source = {"whatever": "42"}
    defn = SchemaDefinition(source)
    assert defn.source == source
    assert defn.name == ""


def test_parse_mapping():
    defn = SchemaDefinition(
        {
            "name": "test",
            "mapping": {"a": "z"},
            "prev_mapping": {"ba": "z"},
            "next_mapping": {"ab": "z"},
            "ending_mapping": {"aa": "zz"},
            "samples": [["aaa", "zzz"], ["baa", "bzz"]],
        }
    )
    defn.parse()
    assert defn.name == "test"
    assert defn.mapping == {"a": "z"}
    assert defn.prev_mapping == {"ba": "z"}
    assert defn.next_mapping == {"ab": "z"}
    assert defn.ending_mapping == {"aa": "zz"}
    assert len(defn.samples) == 2
    assert defn.samples[0] == ["aaa", "zzz"]
    assert defn.samples[1] == ["baa", "bzz"]


def test_invalid_name():
    with pytest.raises(ValueError) as exc:
        defn = SchemaDefinition({})
        defn.parse()
    assert str(exc.value) == ": Missing schema name"


def test_empty_name():
    with pytest.raises(ValueError) as exc:
        defn = SchemaDefinition({"name": ""})
        defn.parse()
    assert str(exc.value) == ": Schema name should not be empty"


def test_invalid_mapping():
    with pytest.raises(ValueError) as exc:
        defn = SchemaDefinition({"name": "test"})
        defn.parse()
    assert str(exc.value) == "test: Missing schema mapping"


def test_empty_mapping():
    defn = SchemaDefinition({"name": "test", "mapping": {}})
    defn.parse()
    assert defn.mapping == {}


def test_invalid_prev_mapping():
    with pytest.raises(ValueError) as exc:
        defn = SchemaDefinition({"name": "test", "mapping": {}, "prev_mapping": "42"})
        defn.parse()
    assert str(exc.value) == "test: Invalid schema prev_mapping: 42"


def test_missing_prev_mapping():
    defn = SchemaDefinition({"name": "test", "mapping": {}})
    defn.parse()
    assert defn.prev_mapping is None


def test_empty_prev_mapping():
    defn = SchemaDefinition({"name": "test", "mapping": {}, "prev_mapping": {}})
    defn.parse()
    assert defn.prev_mapping == {}


def test_invalid_next_mapping():
    with pytest.raises(ValueError) as exc:
        defn = SchemaDefinition({"name": "test", "mapping": {}, "next_mapping": "42"})
        defn.parse()
    assert str(exc.value) == "test: Invalid schema next_mapping: 42"


def test_missing_next_mapping():
    defn = SchemaDefinition({"name": "test", "mapping": {}})
    defn.parse()
    assert defn.next_mapping is None


def test_empty_next_mapping():
    defn = SchemaDefinition({"name": "test", "mapping": {}, "next_mapping": {}})
    defn.parse()
    assert defn.next_mapping == {}


def test_invalid_ending_mapping():
    with pytest.raises(ValueError) as exc:
        defn = SchemaDefinition({"name": "test", "mapping": {}, "ending_mapping": "42"})
        defn.parse()
    assert str(exc.value) == "test: Invalid schema ending_mapping: 42"


def test_missing_ending_mapping():
    defn = SchemaDefinition({"name": "test", "mapping": {}})
    defn.parse()
    assert defn.ending_mapping is None


def test_empty_ending_mapping():
    defn = SchemaDefinition({"name": "test", "mapping": {}, "ending_mapping": {}})
    defn.parse()
    assert defn.ending_mapping == {}


def test_invalid_samples():
    with pytest.raises(ValueError) as exc:
        defn = SchemaDefinition({"name": "test", "mapping": {}, "samples": {}})
        defn.parse()
    assert str(exc.value) == "test: Invalid schema samples: {}"


def test_invalid_sample_not_list():
    with pytest.raises(ValueError) as exc:
        defn = SchemaDefinition({"name": "test", "mapping": {}, "samples": ["42"]})
        defn.parse()
    assert str(exc.value) == "test: Invalid schema sample: 42"


def test_invalid_sample_length():
    with pytest.raises(ValueError) as exc:
        defn = SchemaDefinition({"name": "test", "mapping": {}, "samples": [["aa"]]})
        defn.parse()
    assert str(exc.value) == "test: Invalid schema sample: ['aa']"


def test_invalid_sample_type():
    with pytest.raises(ValueError) as exc:
        defn = SchemaDefinition({"name": "test", "mapping": {}, "samples": [["aa", {}]]})
        defn.parse()
    assert str(exc.value) == "test: Invalid schema sample: ['aa', {}]"


def test_missing_samples():
    defn = SchemaDefinition({"name": "test", "mapping": {}})
    defn.parse()
    assert defn.samples is None


def test_empty_samples():
    defn = SchemaDefinition({"name": "test", "mapping": {}, "samples": []})
    defn.parse()
    assert defn.samples == []
