"""
ALA-LC transliteration schema.
https://dangry.ru/iuliia/ala-lc/
"""

from .schema import Schema, BASE_MAPPING

MAPPING = {
    **BASE_MAPPING,
    **{
        "ё": "ё",
        "ж": "zh",
        "й": "ĭ",
        "х": "kh",
        "ц": "t͡s",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": "ʺ",
        "ы": "y",
        "ь": "ʹ",
        "э": "ė",
        "ю": "i͡u",
        "я": "i͡a",
    },
}

ALT_MAPPING = {
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
        "ъ": '"',
        "ы": "y",
        "ь": "'",
        "э": "e",
        "ю": "iu",
        "я": "ia",
    },
}

ALA_LC = Schema(MAPPING)
ALA_LC_ALT = Schema(ALT_MAPPING)
