"""
Transliterate Cyrillic → Latin in every possible way
"""

# flake8: noqa
from enum import Enum
from iuliia.engine import translate
from iuliia.schema import Schema
from iuliia.wikipedia import WIKIPEDIA
from iuliia.yandexmaps import YANDEX_MAPS
from iuliia.yandexmoney import YANDEX_MONEY

__version__ = "0.5.1"
__all__ = []


class Schemas(Enum):
    """All supported transliteration schemas."""

    wikipedia = WIKIPEDIA
    yandex_maps = YANDEX_MAPS
    yandex_money = YANDEX_MONEY

    @classmethod
    def names(cls):
        """Return sorted list of all supported schemas."""
        return sorted(item.name for item in cls)

    @classmethod
    def get(cls, name):
        """Return schema by its name or ``None`` if nothing found."""
        item = cls.__members__.get(name)
        return item.value if item else None
