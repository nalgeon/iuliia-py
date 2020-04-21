"""
GOST 7.79-2000 (aka ISO 9:1995) transliteration schema.
https://dangry.ru/iuliia/gost-779/
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
        "ё": "yo",
        "ж": "zh",
        "й": "j",
        "х": "x",
        "ц": "cz",
        "ч": "ch",
        "ш": "sh",
        "щ": "shh",
        "ъ": "``",
        "ы": "y`",
        "ь": "`",
        "э": "е`",
        "ю": "yu",
        "я": "ya",
    },
}

ALT_NEXT_MAPPING = {"це": "c", "ци": "c", "цй": "c", "цы": "c"}

GOST_779 = Schema(MAPPING)
GOST_779_ALT = Schema(ALT_MAPPING, next_mapping=ALT_NEXT_MAPPING)
