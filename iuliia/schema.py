"""
Transliteration schema base features.
"""

from .mapping import LetterMapping, PrevMapping, NextMapping, EndingMapping


class Schema:
    """
    Transliteration schema. Defines the way to translate individual letters.
    """

    def __init__(
        self,
        mapping: dict,
        prev_mapping: dict = None,
        next_mapping: dict = None,
        ending_mapping: dict = None,
    ):
        self.map = LetterMapping(mapping)
        self.prev_map = PrevMapping(prev_mapping or {})
        self.next_map = NextMapping(next_mapping or {})
        self.ending_map = EndingMapping(ending_mapping or {})

    def translate_letter(self, prev, curr, next_):
        """Translate ``curr`` letter according to schema mappings.

        ``prev`` (the previous letter) and ``next_`` (the next one)
        are taken into consideration according to corresponding mappings.

        """
        letter = self.prev_map.get(prev + curr)
        if letter is None:
            letter = self.next_map.get(curr + next_)
        if letter is None:
            letter = self.map.get(curr, curr)
        return letter

    def translate_ending(self, ending):
        """Translate word ending according to schema mapping."""
        return self.ending_map.get(ending)
