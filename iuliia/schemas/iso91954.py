"""
ISO/R 9:1954 transliteration schema.
https://dangry.ru/iuliia/iso-9-1954/
"""

from iuliia.mapping import BASE_MAPPING
from iuliia.schema import Schema

MAPPING = {
    **BASE_MAPPING,
    **{
        "ё": "ë",
        "ж": "ž",
        "й": "j",
        "х": "h",
        "ц": "c",
        "ч": "č",
        "ш": "š",
        "щ": "šč",
        "ъ": '"',
        "ы": "y",
        "ь": "ʹ",
        "э": "ė",
        "ю": "ju",
        "я": "ja",
    },
}

ISO_9_1954 = Schema(MAPPING)
