"""
Translate engine.
"""

import re
from typing import Iterator
from .schema import Schema

SPLITTER = re.compile(r"\b")


def translate(source: str, schema: Schema) -> str:
    """
    Translate source Cyrillic string into Latin using specified schema.
    Translates sentences word by word, delegating specifics of transliteration
    to specified schema.
    """
    words = (word for word in SPLITTER.split(source) if word)
    translated = (_translate_word(word, schema) for word in words)
    return "".join(translated)


def _translate_word(word: str, schema: Schema) -> str:
    """Translate word using specified schema."""
    stem, ending = _split_word(word)
    translated_ending = schema.translate_ending(ending)
    if translated_ending:
        # There is a specific translation for the ending,
        # so we need to translate the stem and ending separately.
        translated = _translate_letters(stem, schema)
        translated.append(translated_ending)
    else:
        # There is no specific translation for the ending,
        # so we can translate the whole word at once.
        translated = _translate_letters(word, schema)
    return "".join(translated)


def _translate_letters(word: str, schema: Schema) -> list[str]:
    """Translate letters of a word using specified schema."""
    translated = []
    for prev, curr, next_ in _letter_reader(word):
        letter = schema.translate_letter(prev, curr, next_)
        translated.append(letter)
    return translated


def _split_word(word: str) -> tuple[str, str]:
    """
    Split word into stem and ending.
    Ending is the last two letters of the word.
    """
    ending_length = 2
    if len(word) > ending_length:
        stem = word[:-ending_length]
        ending = word[-ending_length:]
    else:
        stem = word
        ending = ""
    return stem, ending


def _letter_reader(stem: str) -> Iterator[tuple[str, str, str]]:
    """
    Yield letters of a word in (prev, curr, next) tuples.
    E.g. for "word" it will yield:
        ("", "w", "o")
        ("w", "o", "r")
        ("o", "r", "d")
        ("r", "d", "")
    """
    if not stem:
        return
    it = iter(stem)
    prev, curr = "", next(it, "")
    for next_ in it:
        yield prev, curr, next_
        prev, curr = curr, next_
    yield prev, curr, ""
