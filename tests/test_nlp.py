import pytest
import iuliia.nlp as nlp


def test_word_reader():
    it = nlp.word_reader("hello, world")
    assert next(it) == "hello"
    assert next(it) == ", "
    assert next(it) == "world"
    with pytest.raises(StopIteration):
        next(it)

    it = nlp.word_reader("oh, what a :) day!")
    assert next(it) == "oh"
    assert next(it) == ", "
    assert next(it) == "what"
    assert next(it) == " "
    assert next(it) == "a"
    assert next(it) == " :) "
    assert next(it) == "day"
    assert next(it) == "!"
    with pytest.raises(StopIteration):
        next(it)


def test_trigram_reader():
    it = nlp.trigram_reader("word")
    assert next(it) == ("", "w", "o")
    assert next(it) == ("w", "o", "r")
    assert next(it) == ("o", "r", "d")
    assert next(it) == ("r", "d", "")
    with pytest.raises(StopIteration):
        next(it)

    it = nlp.trigram_reader("wo")
    assert next(it) == ("", "w", "o")
    assert next(it) == ("w", "o", "")
    with pytest.raises(StopIteration):
        next(it)

    it = nlp.trigram_reader("w")
    assert next(it) == ("", "w", "")
    with pytest.raises(StopIteration):
        next(it)

    it = nlp.trigram_reader("")
    with pytest.raises(StopIteration):
        next(it)


def test_split_word():
    assert nlp.split_word("word") == ("wo", "rd")
    assert nlp.split_word("w") == ("w", "")
    assert nlp.split_word("") == ("", "")
