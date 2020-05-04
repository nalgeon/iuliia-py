"""
Translate engine.
"""

import re
from .schema import Schema

SPLITTER = re.compile(r"\b")


def translate(source: str, schema: Schema):
    """
    Translate source Cyrillic string into Latin using specified schema.
    Translates sentences word by word, delegating specifics of transliteration
    to specified schema.
    """
    translated = (_translate_word(word, schema) for word in _split_sentence(source))
    return "".join(translated)


def _split_sentence(source: str):
    return (word for word in SPLITTER.split(source) if word)


def _translate_word(word: str, schema: Schema):
    stem, ending = _split_word(word)
    translated_ending = schema.translate_ending(ending) if ending else None
    if translated_ending:
        translated = _translate_letters(stem, schema)
        translated.append(translated_ending)
    else:
        translated = _translate_letters(word, schema)
    return "".join(translated)


def _translate_letters(word, schema):
    translated = []
    for prev, curr, next_ in _letter_reader(word):
        letter = schema.translate_letter(prev, curr, next_)
        translated.append(letter)
    return translated


def _split_word(word):
    ending_length = 2
    if len(word) > ending_length:
        stem = word[:-ending_length]
        ending = word[-ending_length:]
    else:
        stem = word
        ending = ""
    return stem, ending


def _letter_reader(stem):
    idx = 0
    prev = ""
    curr = ""
    next_ = ""
    # pylint: disable=C0200
    for idx in range(0, len(stem)):
        if curr != "":
            prev = curr
        curr = next_ or stem[idx]
        if idx < len(stem) - 1:
            next_ = stem[idx + 1]
        else:
            next_ = ""
        yield prev, curr, next_
