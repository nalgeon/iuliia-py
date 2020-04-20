"""
Transliteration schema base features.
"""


class Mapping:
    """
    Letter map for transliteration schema.
    Provides uppercased mapping automatically.
    """

    def __init__(self, mapping: dict):
        self.map = mapping.copy()
        upper_map = {key.capitalize(): value.capitalize() for key, value in mapping.items()}
        self.map.update(upper_map)

    def get(self, key, default=None):
        """Return mapped value for ``key`` if key is in the map, else ``default``."""
        return self.map.get(key, default)

    def __str__(self):
        return str(self.map)

    def __repr__(self):
        return repr(self.map)


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
        self.map = Mapping(mapping)
        self.prev_map = Mapping(prev_mapping or {})
        self.next_map = Mapping(next_mapping or {})
        self.ending_map = Mapping(ending_mapping or {})

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
