"""
Yandex.Maps transliteration schema.
https://dangry.ru/iuliia/yandex-maps/
"""

from .schema import Schema, BASE_MAPPING

MAPPING = {
    **BASE_MAPPING,
    **{
        "ё": "yo",
        "ж": "zh",
        "й": "y",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "sch",
        "ъ": "",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "yu",
        "я": "ya",
    },
}

NEXT_MAPPING = {"ъе": "y"}

ENDING_MAPPING = {"ый": "iy"}

YANDEX_MAPS = Schema(MAPPING, next_mapping=NEXT_MAPPING, ending_mapping=ENDING_MAPPING)
