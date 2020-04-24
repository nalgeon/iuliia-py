"""
ICAO DOC 9303 transliteration schema.
https://dangry.ru/iuliia/icao-doc-9303/
"""

from iuliia.mapping import BASE_MAPPING
from iuliia.schema import Schema

MAPPING = {
    **BASE_MAPPING,
    **{
        "ё": "e",
        "ж": "zh",
        "й": "i",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": "ie",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "iu",
        "я": "ia",
    },
}

ICAO_DOC_9303 = Schema(MAPPING)
