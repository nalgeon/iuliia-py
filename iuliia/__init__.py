"""
Transliterate Cyrillic → Latin in every possible way
"""

# flake8: noqa
from enum import Enum
from iuliia.engine import translate
from iuliia.schema import Schema
from iuliia.gost16876 import GOST_16876, GOST_16876_ALT
from iuliia.gost52290 import GOST_52290
from iuliia.gost52535 import GOST_52535
from iuliia.gost7034 import GOST_7034
from iuliia.gost779 import GOST_779, GOST_779_ALT
from iuliia.icaodoc9303 import ICAO_DOC_9303
from iuliia.iso91954 import ISO_9_1954
from iuliia.iso91968 import ISO_9_1968, ISO_9_1968_ALT
from iuliia.mvd310 import MVD_310, MVD_310_FR
from iuliia.mvd782 import MVD_782
from iuliia.telegram import TELEGRAM
from iuliia.wikipedia import WIKIPEDIA
from iuliia.yandexmaps import YANDEX_MAPS
from iuliia.yandexmoney import YANDEX_MONEY

__version__ = "0.7.0"
__all__ = []


class Schemas(Enum):
    """All supported transliteration schemas."""

    gost_16876 = GOST_16876
    gost_16876_alt = GOST_16876_ALT
    gost_52290 = GOST_52290
    gost_52535 = GOST_52535
    gost_7034 = GOST_7034
    gost_779 = GOST_779
    gost_779_alt = GOST_779_ALT
    icao_doc_9303 = ICAO_DOC_9303
    iso_9 = GOST_779
    iso_9_1954 = ISO_9_1954
    iso_9_1968 = ISO_9_1968
    iso_9_1968_alt = ISO_9_1968_ALT
    mvd_310 = MVD_310
    mvd_310_fr = MVD_310_FR
    mvd_782 = MVD_782
    telegram = TELEGRAM
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
