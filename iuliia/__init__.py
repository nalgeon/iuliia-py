"""
Transliterate Cyrillic → Latin in every possible way
"""

# flake8: noqa
from .engine import translate
from .schema import Schema
from .schemas import Schemas

__version__ = "0.11.4"
__all__ = []  # type: ignore

ALA_LC = Schemas.ala_lc.value  # type: ignore
ALA_LC_ALT = Schemas.ala_lc_alt.value  # type: ignore
BGN_PCGN = Schemas.bgn_pcgn.value  # type: ignore
BGN_PCGN_ALT = Schemas.bgn_pcgn_alt.value  # type: ignore
BS_2979 = Schemas.bs_2979.value  # type: ignore
BS_2979_ALT = Schemas.bs_2979_alt.value  # type: ignore
GOST_16876 = Schemas.gost_16876.value  # type: ignore
GOST_16876_ALT = Schemas.gost_16876_alt.value  # type: ignore
GOST_52290 = Schemas.gost_52290.value  # type: ignore
GOST_52535 = Schemas.gost_52535.value  # type: ignore
GOST_7034 = Schemas.gost_7034.value  # type: ignore
GOST_779 = Schemas.gost_779.value  # type: ignore
GOST_779_ALT = Schemas.gost_779_alt.value  # type: ignore
ICAO_DOC_9303 = Schemas.icao_doc_9303.value  # type: ignore
ISO_9_1954 = Schemas.iso_9_1954.value  # type: ignore
ISO_9_1968 = Schemas.iso_9_1968.value  # type: ignore
ISO_9_1968_ALT = Schemas.iso_9_1968_alt.value  # type: ignore
MOSMETRO = Schemas.mosmetro.value  # type: ignore
MVD_310 = Schemas.mvd_310.value  # type: ignore
MVD_310_FR = Schemas.mvd_310_fr.value  # type: ignore
MVD_782 = Schemas.mvd_782.value  # type: ignore
SCIENTIFIC = Schemas.scientific.value  # type: ignore
TELEGRAM = Schemas.telegram.value  # type: ignore
UNGEGN_1987 = Schemas.ungegn_1987.value  # type: ignore
WIKIPEDIA = Schemas.wikipedia.value  # type: ignore
YANDEX_MAPS = Schemas.yandex_maps.value  # type: ignore
YANDEX_MONEY = Schemas.yandex_money.value  # type: ignore
