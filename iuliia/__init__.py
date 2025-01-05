"""
Transliterate Cyrillic → Latin in every possible way
"""

from .engine import translate
from .repo import FileRepo
from .schema import Schema

__all__ = [
    "translate",
    "FileRepo",
    "Schema",
    "schemas",
    "ALA_LC",
    "ALA_LC_ALT",
    "BGN_PCGN",
    "BGN_PCGN_ALT",
    "BS_2979",
    "BS_2979_ALT",
    "GOST_16876",
    "GOST_16876_ALT",
    "GOST_52290",
    "GOST_52535",
    "GOST_7034",
    "GOST_779",
    "GOST_779_ALT",
    "ICAO_DOC_9303",
    "ISO_9_1954",
    "ISO_9_1968",
    "ISO_9_1968_ALT",
    "MOSMETRO",
    "MVD_310",
    "MVD_310_FR",
    "MVD_782",
    "SCIENTIFIC",
    "TELEGRAM",
    "UNGEGN_1987",
    "UZ",
    "WIKIPEDIA",
    "YANDEX_MAPS",
    "YANDEX_MONEY",
]

schemas = FileRepo()

ALA_LC: Schema = schemas.get("ala_lc")
ALA_LC_ALT: Schema = schemas.get("ala_lc_alt")
BGN_PCGN: Schema = schemas.get("bgn_pcgn")
BGN_PCGN_ALT: Schema = schemas.get("bgn_pcgn_alt")
BS_2979: Schema = schemas.get("bs_2979")
BS_2979_ALT: Schema = schemas.get("bs_2979_alt")
GOST_16876: Schema = schemas.get("gost_16876")
GOST_16876_ALT: Schema = schemas.get("gost_16876_alt")
GOST_52290: Schema = schemas.get("gost_52290")
GOST_52535: Schema = schemas.get("gost_52535")
GOST_7034: Schema = schemas.get("gost_7034")
GOST_779: Schema = schemas.get("gost_779")
GOST_779_ALT: Schema = schemas.get("gost_779_alt")
ICAO_DOC_9303: Schema = schemas.get("icao_doc_9303")
ISO_9_1954: Schema = schemas.get("iso_9_1954")
ISO_9_1968: Schema = schemas.get("iso_9_1968")
ISO_9_1968_ALT: Schema = schemas.get("iso_9_1968_alt")
MOSMETRO: Schema = schemas.get("mosmetro")
MVD_310: Schema = schemas.get("mvd_310")
MVD_310_FR: Schema = schemas.get("mvd_310_fr")
MVD_782: Schema = schemas.get("mvd_782")
SCIENTIFIC: Schema = schemas.get("scientific")
TELEGRAM: Schema = schemas.get("telegram")
UNGEGN_1987: Schema = schemas.get("ungegn_1987")
UZ: Schema = schemas.get("uz")
WIKIPEDIA: Schema = schemas.get("wikipedia")
YANDEX_MAPS: Schema = schemas.get("yandex_maps")
YANDEX_MONEY: Schema = schemas.get("yandex_money")
