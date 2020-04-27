"""
Transliteration schema registry.
"""

import json
from pathlib import Path
from enum import Enum
from typing import List
from iuliia.schema import Schema


def _schema_loader():
    return (Schema.load(defn) for defn in _definition_reader())


def _definition_reader():
    schemas_path = Path(__file__).parent / "schemas"
    if not schemas_path.exists():
        raise ValueError(f"Schema path does not exist: {schemas_path}")
    paths = schemas_path.glob("*.json")
    for path in paths:
        definition = _load_definition(path)
        yield definition


def _load_definition(path):
    with open(path) as file:
        return json.load(file)


class _Schemas(Enum):
    """Base class for supported transliteration schemas."""

    @classmethod
    def names(cls) -> List[str]:
        """Return sorted list of all supported schemas."""
        return sorted(item.name for item in cls)

    @classmethod
    def get(cls, name: str) -> Schema:
        """Return schema by its name or ``None`` if nothing found."""
        item = cls.__members__.get(name)
        return item.value if item else None


# All supported transliteration schemas
# pylint: disable=invalid-name
Schemas = Enum("Schemas", [(schema.name, schema) for schema in _schema_loader()], type=_Schemas)
