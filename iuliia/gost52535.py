"""
GOST R 52535.1-2006 transliteration schema.
http://localhost:3000/iuliia/gost-52535/
"""

from .schema import Schema, BASE_MAPPING

MAPPING = {
    **BASE_MAPPING,
    **{
        "ё": "e",
        "ж": "zh",
        "й": "i",
        "х": "kh",
        "ц": "tc",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": "",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "iu",
        "я": "ia",
    },
}

GOST_52535 = Schema(MAPPING)
