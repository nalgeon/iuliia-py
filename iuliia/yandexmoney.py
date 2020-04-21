"""
Yandex.Money transliteration schema.
https://dangry.ru/iuliia/yandex-money/
"""

from .schema import Schema, BASE_MAPPING

MAPPING = {
    **BASE_MAPPING,
    **{
        "ё": "e",
        "ж": "zh",
        "й": "i",
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

YANDEX_MONEY = Schema(MAPPING)
