"""
Transliterate Cyrillic → Latin in all ways possible
"""

# flake8: noqa
from enum import Enum
from iuliia.engine import translate
from iuliia.schema import Schema
from iuliia.yandexmoney import YANDEX_MONEY


class Schemas(Enum):
    """All supported transliteration schemas."""

    yandex_money = YANDEX_MONEY


__version__ = "0.3.0"
__all__ = []
