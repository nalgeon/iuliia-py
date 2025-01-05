"""
File-based schema repository.
"""

import json
from pathlib import Path
from .schema import Schema, TranslitSchema
from .validator import Validator

SCHEMA_DIR = Path(__file__).parent / "schemas"


class FileSchema:
    """
    File-based transliteration schema.
    Translates Cyrillic text into Latin using a given set of rules (mappings).
    Lazy loads schema from JSON file as needed.
    """

    def __init__(self, name: str, path: str | Path):
        self.name = name
        self.path = Path(path)
        self._schema: TranslitSchema | None = None

    @property
    def description(self) -> str | None:
        """Schema description."""
        if self._schema is None:
            self._schema = self._load()
        return self._schema.description

    @property
    def samples(self) -> list[list[str]]:
        """Schema samples."""
        if self._schema is None:
            self._schema = self._load()
        return self._schema.samples

    def translate(self, source: str) -> str:
        """
        Translate source Cyrillic string into Latin.
        Translates the source string word by word.
        """
        if self._schema is None:
            self._schema = self._load()
        return self._schema.translate(source)

    def _load(self) -> TranslitSchema:
        """Load schema by its name."""
        if not self.path.exists():
            raise ValueError(f"Schema path does not exist: {self.path}")

        # Load and validate schema definition.
        defn = {}
        with open(self.path, encoding="utf-8") as file:
            defn = json.load(file)
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

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}')"


class FileRepo:
    """
    File-based transliteration schema repository.
    """

    def __init__(self, base_dir: str | Path = SCHEMA_DIR):
        self.base_dir = base_dir
        self.schemas = {}
        for path in Path(base_dir).iterdir():
            if not path.suffix == ".json":
                continue
            name = path.stem
            self.schemas[name] = FileSchema(name, path)

    def has(self, name: str) -> bool:
        """Check if schema exists."""
        return name in self.schemas

    def get(self, name: str) -> Schema:
        """Get schema by name."""
        if name not in self.schemas:
            raise ValueError(f"Schema not found: {name}")
        return self.schemas[name]

    def names(self) -> list[str]:
        """Return schema names sorted by name."""
        return sorted(self.schemas.keys())

    def items(self) -> list[tuple[str, Schema]]:
        """Return (name, schema) tuples sorted by name."""
        return sorted(self.schemas.items(), key=lambda item: item[0])
