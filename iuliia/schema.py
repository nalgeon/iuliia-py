"""
Transliteration schema base features.
"""

BASE_MAPPING = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "з": "z",
    "и": "i",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
}


class Mapping:
    """Letter map for transliteration schema."""

    def __init__(self, mapping: dict):
        self.map = mapping.copy()

    def get(self, key, default=None):
        """Return mapped value for ``key`` if key is in the map, else ``default``."""
        return self.map.get(key, default)

    def __str__(self):
        return str(self.map)

    def __repr__(self):
        return repr(self.map)


class LetterMapping(Mapping):
    """Mapping for individual letters."""

    def __init__(self, mapping: dict):
        super().__init__(mapping)
        upper_map = {key.capitalize(): value.capitalize() for key, value in mapping.items()}
        self.map.update(upper_map)


class PrevMapping(Mapping):
    """Mapping for letters with respect to previous sibling."""

    def __init__(self, mapping: dict):
        super().__init__(mapping)
        upper_map_1 = {key.capitalize(): value for key, value in mapping.items()}
        upper_map_2 = {key.upper(): value.capitalize() for key, value in mapping.items()}
        self.map.update(upper_map_1)
        self.map.update(upper_map_2)


class NextMapping(Mapping):
    """Mapping for letters with respect to next sibling."""

    def __init__(self, mapping: dict):
        super().__init__(mapping)
        upper_map_1 = {key.capitalize(): value.capitalize() for key, value in mapping.items()}
        upper_map_2 = {key.upper(): value.capitalize() for key, value in mapping.items()}
        self.map.update(upper_map_1)
        self.map.update(upper_map_2)


class EndingMapping(Mapping):
    """Mapping for word endings."""

    def __init__(self, mapping: dict):
        super().__init__(mapping)
        upper_map = {key.upper(): value.upper() for key, value in mapping.items()}
        self.map.update(upper_map)


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
