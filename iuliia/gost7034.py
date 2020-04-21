"""
GOST R 7.0.34-2014 transliteration schema.
http://localhost:3000/iuliia/gost-7034/
"""

from .schema import Schema, BASE_MAPPING

MAPPING = {
    **BASE_MAPPING,
    **{
        "ё": "yo",
        "ж": "zh",
        "й": "j",
        "х": "x",
        "ц": "c",
        "ч": "ch",
        "ш": "sh",
        "щ": "shh",
        "ъ": "''",
        "ы": "y",
        "ь": "'",
        "э": "e",
        "ю": "yu",
        "я": "ya",
    },
}

GOST_7034 = Schema(MAPPING)
