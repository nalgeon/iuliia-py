"""
Scientific transliteration schema.
https://dangry.ru/iuliia/scientific/
"""

from iuliia.mapping import BASE_MAPPING
from iuliia.schema import Schema

MAPPING = {
    **BASE_MAPPING,
    **{
        "ё": "ё",
        "ж": "ž",
        "й": "j",
        "х": "x",
        "ц": "c",
        "ч": "č",
        "ш": "š",
        "щ": "šč",
        "ъ": "ʺ",
        "ы": "y",
        "ь": "ʹ",
        "э": "è",
        "ю": "ju",
        "я": "ja",
    },
}

SCIENTIFIC = Schema(MAPPING)
