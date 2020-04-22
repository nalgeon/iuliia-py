"""
ISO/R 9:1968 transliteration schema.
https://dangry.ru/iuliia/iso-9-1968/
"""

from .schema import Schema, BASE_MAPPING

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
        "ъ": "ʺ",
        "ы": "y",
        "ь": "ʹ",
        "э": "ė",
        "ю": "ju",
        "я": "ja",
    },
}

ALT_MAPPING = {
    **BASE_MAPPING,
    **{
        "ё": "ë",
        "ж": "zh",
        "и": "y",
        "й": "ĭ",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": "ʺ",
        "ы": "y",
        "ь": "ʹ",
        "э": "ė",
        "ю": "yu",
        "я": "ya",
    },
}

ISO_9_1968 = Schema(MAPPING)
ISO_9_1968_ALT = Schema(ALT_MAPPING)
