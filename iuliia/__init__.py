"""
Transliterate Cyrillic → Latin in every possible way
"""

# flake8: noqa
from .engine import translate
from .schema import Schema
from .schemas import Schemas

__version__ = "0.10.0"
__all__ = []

ALA_LC = Schemas.ala_lc.value
ALA_LC_ALT = Schemas.ala_lc_alt.value
BGN_PCGN = Schemas.bgn_pcgn.value
BGN_PCGN_ALT = Schemas.bgn_pcgn_alt.value
BS_2979 = Schemas.bs_2979.value
BS_2979_ALT = Schemas.bs_2979_alt.value
GOST_16876 = Schemas.gost_16876.value
GOST_16876_ALT = Schemas.gost_16876_alt.value
GOST_52290 = Schemas.gost_52290.value
GOST_52535 = Schemas.gost_52535.value
GOST_7034 = Schemas.gost_7034.value
GOST_779 = Schemas.gost_779.value
GOST_779_ALT = Schemas.gost_779_alt.value
ICAO_DOC_9303 = Schemas.icao_doc_9303.value
ISO_9_1954 = Schemas.iso_9_1954.value
ISO_9_1968 = Schemas.iso_9_1968.value
ISO_9_1968_ALT = Schemas.iso_9_1968_alt.value
MOSMETRO = Schemas.mosmetro.value
MVD_310 = Schemas.mvd_310.value
MVD_310_FR = Schemas.mvd_310_fr.value
MVD_782 = Schemas.mvd_782.value
SCIENTIFIC = Schemas.scientific.value
TELEGRAM = Schemas.telegram.value
UNGEGN_1987 = Schemas.ungegn_1987.value
WIKIPEDIA = Schemas.wikipedia.value
YANDEX_MAPS = Schemas.yandex_maps.value
YANDEX_MONEY = Schemas.yandex_money.value
