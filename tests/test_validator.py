import pytest
from iuliia.validator import Validator


def test_valid():
    Validator(
        {
            "name": "test",
            "mapping": {"a": "z"},
            "prev_mapping": {"ba": "z"},
            "next_mapping": {"ab": "z"},
            "ending_mapping": {"aa": "zz"},
            "samples": [["aaa", "zzz"], ["baa", "bzz"]],
        }
    ).run()


def test_invalid_name():
    with pytest.raises(ValueError) as exc:
        Validator({}).run()
    assert str(exc.value) == "<unknown>: Missing schema name"


def test_empty_name():
    with pytest.raises(ValueError) as exc:
        Validator({"name": ""}).run()
    assert str(exc.value) == ": Schema name should not be empty"


def test_invalid_mapping():
    with pytest.raises(ValueError) as exc:
        Validator({"name": "test"}).run()
    assert str(exc.value) == "test: Missing schema mapping"


def test_empty_mapping():
    Validator({"name": "test", "mapping": {}}).run()


def test_invalid_prev_mapping():
    with pytest.raises(ValueError) as exc:
        Validator({"name": "test", "mapping": {}, "prev_mapping": "42"}).run()
    assert str(exc.value) == "test: Invalid schema prev_mapping: 42"


def test_missing_prev_mapping():
    Validator({"name": "test", "mapping": {}, "prev_mapping": {}}).run()
    Validator({"name": "test", "mapping": {}}).run()


def test_invalid_next_mapping():
    with pytest.raises(ValueError) as exc:
        Validator({"name": "test", "mapping": {}, "next_mapping": "42"}).run()
    assert str(exc.value) == "test: Invalid schema next_mapping: 42"


def test_missing_next_mapping():
    Validator({"name": "test", "mapping": {}, "next_mapping": {}}).run()
    Validator({"name": "test", "mapping": {}}).run()


def test_invalid_ending_mapping():
    with pytest.raises(ValueError) as exc:
        Validator({"name": "test", "mapping": {}, "ending_mapping": "42"}).run()
    assert str(exc.value) == "test: Invalid schema ending_mapping: 42"


def test_missing_ending_mapping():
    Validator({"name": "test", "mapping": {}, "ending_mapping": {}}).run()
    Validator({"name": "test", "mapping": {}}).run()


def test_invalid_samples():
    with pytest.raises(ValueError) as exc:
        Validator({"name": "test", "mapping": {}, "samples": {}}).run()
    assert str(exc.value) == "test: Invalid schema samples: {}"


def test_invalid_sample_not_list():
    with pytest.raises(ValueError) as exc:
        Validator({"name": "test", "mapping": {}, "samples": ["42"]}).run()
    assert str(exc.value) == "test: Invalid schema sample: 42"


def test_invalid_sample_length():
    with pytest.raises(ValueError) as exc:
        Validator({"name": "test", "mapping": {}, "samples": [["aa"]]}).run()
    assert str(exc.value) == "test: Invalid schema sample: ['aa']"


def test_invalid_sample_type():
    with pytest.raises(ValueError) as exc:
        Validator({"name": "test", "mapping": {}, "samples": [["aa", {}]]}).run()
    assert str(exc.value) == "test: Invalid schema sample: ['aa', {}]"


def test_missing_samples():
    Validator({"name": "test", "mapping": {}, "samples": []}).run()
    Validator({"name": "test", "mapping": {}}).run()
