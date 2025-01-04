import pytest
import iuliia.engine as engine


def test_split_word():
    assert engine._split_word("word") == ("wo", "rd")
    assert engine._split_word("w") == ("w", "")
    assert engine._split_word("") == ("", "")


def test_letter_reader():
    it = engine._letter_reader("word")
    assert next(it) == ("", "w", "o")
    assert next(it) == ("w", "o", "r")
    assert next(it) == ("o", "r", "d")
    assert next(it) == ("r", "d", "")
    with pytest.raises(StopIteration):
        next(it)

    it = engine._letter_reader("wo")
    assert next(it) == ("", "w", "o")
    assert next(it) == ("w", "o", "")
    with pytest.raises(StopIteration):
        next(it)

    it = engine._letter_reader("w")
    assert next(it) == ("", "w", "")
    with pytest.raises(StopIteration):
        next(it)

    it = engine._letter_reader("")
    with pytest.raises(StopIteration):
        next(it)
