"""
Transliteration schema base features.
"""

from .mapping import LetterMapping, PrevMapping, NextMapping, EndingMapping


class Schema:
    """
    Transliteration schema. Defines the way to translate individual letters.
    """

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        name: str,
        mapping: dict,
        prev_mapping: dict = None,
        next_mapping: dict = None,
        ending_mapping: dict = None,
        samples: list = None,
    ):
        self.name = name
        self.map = LetterMapping(mapping)
        self.prev_map = PrevMapping(prev_mapping or {})
        self.next_map = NextMapping(next_mapping or {})
        self.ending_map = EndingMapping(ending_mapping or {})
        self.samples = samples or []

    def translate_letter(self, prev: str, curr: str, next_: str) -> str:
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

    def translate_ending(self, ending: str) -> str:
        """Translate word ending according to schema mapping."""
        return self.ending_map.get(ending)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    @classmethod
    def load(cls, definition: dict):
        """Load schema from definition."""
        defn = SchemaDefinition(definition)
        defn.parse()
        return Schema(
            name=defn.name,
            mapping=defn.mapping,
            prev_mapping=defn.prev_mapping,
            next_mapping=defn.next_mapping,
            ending_mapping=defn.ending_mapping,
            samples=defn.samples,
        )


class SchemaDefinition:
    """Translitiration schema definition."""

    def __init__(self, source: dict):
        self.source = source
        self.name = None
        self.mapping = None
        self.prev_mapping = None
        self.next_mapping = None
        self.ending_mapping = None
        self.samples = None

    def parse(self):
        """Parse source definition, raising ValueError if necessary."""
        self._parse_name()
        self._parse_mapping("mapping")
        self._parse_mapping_or_none("prev_mapping")
        self._parse_mapping_or_none("next_mapping")
        self._parse_mapping_or_none("ending_mapping")
        self._parse_samples()

    def _parse_name(self):
        name = self.source.get("name")
        if not name or not isinstance(name, str):
            raise ValueError(f"Invalid schema name: {name}")
        self.name = name

    def _parse_mapping(self, mapping_name: str):
        mapping = self.source.get(mapping_name)
        if mapping is None or not isinstance(mapping, dict):
            raise ValueError(f"{self.name}: Invalid {mapping_name}: {mapping}")
        setattr(self, mapping_name, mapping)

    def _parse_mapping_or_none(self, mapping_name: str):
        mapping = self.source.get(mapping_name)
        if mapping is not None and not isinstance(mapping, dict):
            raise ValueError(f"{self.name}: Invalid {mapping_name}: {mapping}")
        setattr(self, mapping_name, mapping)

    def _parse_samples(self):
        samples = self.source.get("samples")
        if samples is not None and not isinstance(samples, list):
            raise ValueError(f"{self.name}: Invalid samples: {samples}")
        if samples:
            for sample in samples:
                self._raise_on_invalid_sample(sample)
        self.samples = samples

    def _raise_on_invalid_sample(self, sample):
        message = f"{self.name}: Invalid sample: {sample}"
        if not isinstance(sample, list):
            raise ValueError(message)
        if len(sample) != 2:
            raise ValueError(message)
        if not isinstance(sample[0], str) or not isinstance(sample[1], str):
            raise ValueError(message)
