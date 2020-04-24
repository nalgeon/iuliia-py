"""
Transliterate Cyrillic → Latin in every possible way
"""

# flake8: noqa
from .engine import translate
from .schema import Schema
from .schemas import (
    Schemas,
    ALA_LC,
    ALA_LC_ALT,
    BGN_PCGN,
    BGN_PCGN_ALT,
    BS_2979,
    BS_2979_ALT,
    GOST_16876,
    GOST_16876_ALT,
    GOST_52290,
    GOST_52535,
    GOST_7034,
    GOST_779,
    GOST_779_ALT,
    ICAO_DOC_9303,
    ISO_9_1954,
    ISO_9_1968,
    ISO_9_1968_ALT,
    MVD_310,
    MVD_310_FR,
    MVD_782,
    SCIENTIFIC,
    TELEGRAM,
    UNGEGN_1987,
    WIKIPEDIA,
    YANDEX_MAPS,
    YANDEX_MONEY,
)

__version__ = "0.9.0"
__all__ = []
