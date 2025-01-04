"""
Lazy schema loader.
"""

import json
from pathlib import Path
from .schema import TranslitSchema
from .validator import Validator


class Loader:
    """Loads transliteration schemas from JSON files."""

    def __init__(self):
        self.base_path = Path(__file__).parent / "schemas"

    def load(self, name: str) -> TranslitSchema:
        """Load schema by its name."""
        path = self.base_path / f"{name}.json"
        if not path.exists():
            raise ValueError(f"Schema path does not exist: {path}")
        defn = self._load_definition(path)
        Validator(defn).run()
        return TranslitSchema(
            name=defn.get("name", ""),
            description=defn.get("description"),
            mapping=defn.get("mapping", {}),
            prev_mapping=defn.get("prev_mapping"),
            next_mapping=defn.get("next_mapping"),
            ending_mapping=defn.get("ending_mapping"),
            samples=defn.get("samples"),
        )

    def _load_definition(self, path: str | Path) -> dict:
        with open(path, encoding="utf-8") as file:
            return json.load(file)


class LazySchema:
    """
    Transliteration schema. Translates Cyrillic text into Latin
    using a given set of rules (mappings).
    Lazy loads schema from JSON file as needed.
    """

    def __init__(self, name: str):
        self.name = name
        self._loader = Loader()
        self._schema: TranslitSchema | None = None

    @property
    def description(self) -> str | None:
        """Schema description."""
        if self._schema is None:
            self._schema = self._loader.load(self.name)
        return self._schema.description

    @property
    def samples(self) -> list[list[str]]:
        """Schema samples."""
        if self._schema is None:
            self._schema = self._loader.load(self.name)
        return self._schema.samples

    def translate(self, source: str) -> str:
        """
        Translate source Cyrillic string into Latin.
        Translates the source string word by word.
        """
        if self._schema is None:
            self._schema = self._loader.load(self.name)
        return self._schema.translate(source)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}')"
