"""
Specific transliteration schemas.
"""

from enum import Enum
from .alalc import ALA_LC, ALA_LC_ALT
from .bgnpcgn import BGN_PCGN, BGN_PCGN_ALT
from .bs2979 import BS_2979, BS_2979_ALT
from .gost16876 import GOST_16876, GOST_16876_ALT
from .gost52290 import GOST_52290
from .gost52535 import GOST_52535
from .gost7034 import GOST_7034
from .gost779 import GOST_779, GOST_779_ALT
from .icaodoc9303 import ICAO_DOC_9303
from .iso91954 import ISO_9_1954
from .iso91968 import ISO_9_1968, ISO_9_1968_ALT
from .mvd310 import MVD_310, MVD_310_FR
from .mvd782 import MVD_782
from .scientific import SCIENTIFIC
from .telegram import TELEGRAM
from .ungegn1987 import UNGEGN_1987
from .wikipedia import WIKIPEDIA
from .yandexmaps import YANDEX_MAPS
from .yandexmoney import YANDEX_MONEY


class Schemas(Enum):
    """All supported transliteration schemas."""

    ala_lc = ALA_LC
    ala_lc_alt = ALA_LC_ALT
    bgn_pcgn = BGN_PCGN
    bgn_pcgn_alt = BGN_PCGN_ALT
    bs_2979 = BS_2979
    bs_2979_alt = BS_2979_ALT
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
    scientific = SCIENTIFIC
    telegram = TELEGRAM
    ungegn_1987 = UNGEGN_1987
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
