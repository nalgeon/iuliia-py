"""
Natural language processing utilities.
"""

import re
from typing import Iterator

SPLITTER = re.compile(r"\b")


def word_reader(sentence: str) -> Iterator[str]:
    """
    Yield parts of a sentence, splitting by word boundaries.
    E.g. for "hello, world!" it will yield:
        "hello"
        ", "
        "world"
        "!"
    """
    return (word for word in SPLITTER.split(sentence) if word)


def trigram_reader(word: str) -> Iterator[tuple[str, str, str]]:
    """
    Yield letters of a word in (prev, curr, next) tuples.
    E.g. for "word" it will yield:
        ("", "w", "o")
        ("w", "o", "r")
        ("o", "r", "d")
        ("r", "d", "")
    """
    if not word:
        return
    it = iter(word)
    prev, curr = "", next(it, "")
    for next_ in it:
        yield prev, curr, next_
        prev, curr = curr, next_
    yield prev, curr, ""


def split_word(word: str) -> tuple[str, str]:
    """
    Split word into stem and ending (the last two letters of the word).
    If the word has two or fewer letters, the ending is empty.
    """
    ending_len = 2
    if len(word) <= ending_len:
        return word, ""
    stem = word[:-ending_len]
    ending = word[-ending_len:]
    return stem, ending
