"""
GOST R 7.0.34-2014 transliteration schema.
http://localhost:3000/iuliia/gost-7034/
"""

from iuliia.mapping import BASE_MAPPING
from iuliia.schema import Schema

# This schema defines alternatives for many letters, but does not specify when to use which.
# Therefore, `iuliia` uses the first of suggested translations for each such letter.
MAPPING = {
    **BASE_MAPPING,
    **{
        "е": "e",  # (ye)
        "ё": "yo",  # (jo)
        "ж": "zh",
        "й": "j",  # (i,y)
        "х": "x",  # (kh)
        "ц": "c",  # (tz,cz)
        "ч": "ch",
        "ш": "sh",
        "щ": "shh",
        "ъ": "''",  # (empty)
        "ы": "y",
        "ь": "'",  # (empty)
        "э": "e",
        "ю": "yu",  # (ju)
        "я": "ya",  # (ja)
    },
}

GOST_7034 = Schema(MAPPING)
