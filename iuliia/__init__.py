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


class Schemas(Enum):
    """All supported transliteration schemas."""

    wikipedia = WIKIPEDIA
    yandex_maps = YANDEX_MAPS
    yandex_money = YANDEX_MONEY


__version__ = "0.5.0"
__all__ = []
