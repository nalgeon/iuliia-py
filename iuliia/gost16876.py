"""
GOST 16876-71 (aka GOST 1983) transliteration schema.
https://dangry.ru/iuliia/gost-16876/
"""

from .schema import Schema, BASE_MAPPING

MAPPING = {
    **BASE_MAPPING,
    **{
        "ё": "ё",
        "ж": "ž",
        "й": "j",
        "х": "h",
        "ц": "c",
        "ч": "č",
        "ш": "š",
        "щ": "ŝ",
        "ъ": "ʺ",
        "ы": "y",
        "ь": "ʹ",
        "э": "è",
        "ю": "û",
        "я": "â",
    },
}

ALT_MAPPING = {
    **BASE_MAPPING,
    **{
        "ё": "jo",
        "ж": "zh",
        "й": "jj",
        "х": "kh",
        "ц": "c",
        "ч": "ch",
        "ш": "sh",
        "щ": "shh",
        "ъ": '"',
        "ы": "y",
        "ь": "'",
        "э": "eh",
        "ю": "ju",
        "я": "ja",
    },
}

GOST_16876 = Schema(MAPPING)
GOST_16876_ALT = Schema(ALT_MAPPING)
