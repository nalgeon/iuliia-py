"""
Telegram transliteration schema.
https://dangry.ru/iuliia/telegram/
"""

from .schema import Schema, BASE_MAPPING

MAPPING = {
    **BASE_MAPPING,
    **{
        "ё": "e",
        "ж": "j",
        "й": "i",
        "х": "h",
        "ц": "c",
        "ч": "ch",
        "ш": "sh",
        "щ": "sc",
        "ъ": "",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "iu",
        "я": "ia",
    },
}

TELEGRAM = Schema(MAPPING)
