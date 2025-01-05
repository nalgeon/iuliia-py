"""
Transliteration schema.
"""

from typing import Protocol
from . import nlp


class Schema(Protocol):
    """
    Transliteration schema. Translates Cyrillic text into Latin
    using a given set of rules (mappings).
    """

    @property
    def name(self) -> str | None:
        """Schema name."""

    @property
    def description(self) -> str | None:
        """Schema description."""

    @property
    def samples(self) -> list[list[str]]:
        """Schema samples."""

    def translate(self, source: str) -> str:
        """
        Translate source Cyrillic string into Latin.
        Translates the source string word by word.
        """


class TranslitSchema:
    """
    Transliteration schema. Translates Cyrillic text into Latin
    using a given set of rules (mappings).
    """

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        *,
        name: str,
        mapping: dict[str, str],
        prev_mapping: dict[str, str] | None = None,
        next_mapping: dict[str, str] | None = None,
        ending_mapping: dict[str, str] | None = None,
        samples: list[list[str]] | None = None,
        description: str | None = None,
    ):
        self.name = name
        self.description = description
        self.samples = samples or []

        # Mapping for individual letters.
        # - current letter is lowercase -> do not change case
        self.map = dict(mapping.items())
        # - current letter is uppercase -> uppercase
        self.map |= {key.capitalize(): val.capitalize() for key, val in mapping.items()}

        # Mapping for letters with respect to previous sibling.
        prev_mapping = prev_mapping or {}
        # - both letters are lowercase -> do not change case
        self.prev_map = dict(prev_mapping.items())
        # - previous is uppercase, current is lowercase -> do not change case
        self.prev_map |= {key.capitalize(): val for key, val in prev_mapping.items()}
        # - previous and current are uppercase -> capitalize
        self.prev_map |= {key.upper(): val.capitalize() for key, val in prev_mapping.items()}

        # Mapping for letters with respect to next sibling.
        next_mapping = next_mapping or {}
        # - both letters are lowercase -> do not change case
        self.next_map = dict(next_mapping.items())
        # - current is uppercase, next is lowercase -> capitalize
        self.next_map |= {key.capitalize(): val.capitalize() for key, val in next_mapping.items()}
        # - current and next are uppercase -> capitalize
        self.next_map |= {key.upper(): val.capitalize() for key, val in next_mapping.items()}

        # Mapping for word endings.
        ending_mapping = ending_mapping or {}
        # - ending is lowercase -> do not change case
        self.ending_map = dict(ending_mapping.items())
        # - ending is uppercase -> uppercase
        self.ending_map |= {key.upper(): val.upper() for key, val in ending_mapping.items()}

    def translate(self, source: str) -> str:
        """
        Translate source Cyrillic string into Latin.
        Translates the source string word by word.
        """
        words = nlp.word_reader(source)
        translated = (self._translate_word(word) for word in words)
        return "".join(translated)

    def _translate_word(self, word: str) -> str:
        """Translate a single word."""
        stem, ending = nlp.split_word(word)
        translated_ending = self._translate_ending(ending)
        if translated_ending:
            # There is a specific translation for the ending,
            # so we need to translate the stem and ending separately.
            translated = self._translate_letters(stem)
            translated.append(translated_ending)
        else:
            # There is no specific translation for the ending,
            # so we can translate the whole word at once.
            translated = self._translate_letters(word)
        return "".join(translated)

    def _translate_letters(self, word: str) -> list[str]:
        """Translate letters of a single word."""
        translated = []
        for prev, curr, next_ in nlp.trigram_reader(word):
            letter = self._translate_letter(prev, curr, next_)
            translated.append(letter)
        return translated

    def _translate_letter(self, prev: str, curr: str, next_: str) -> str:
        """Translate a single letter curr according to schema mapping.

        prev (the previous letter) and next_ (the next one)
        are considered according to their mappings.
        """
        letter = self.prev_map.get(prev + curr)
        if letter is None:
            letter = self.next_map.get(curr + next_)
        if letter is None:
            letter = self.map.get(curr)
        if letter is None:
            letter = curr
        return letter

    def _translate_ending(self, ending: str) -> str | None:
        """Translate word ending according to schema mapping."""
        if not ending:
            return None
        return self.ending_map.get(ending)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}')"
