"""
MVD 310-1997 transliteration schema.
https://dangry.ru/iuliia/mvd-310/
"""

from .schema import Schema, BASE_MAPPING

EN_MAPPING = {
    **BASE_MAPPING,
    **{
        "ё": "e",
        "ж": "zh",
        "й": "y",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": '"',
        "ы": "y",
        "ь": "'",
        "э": "e",
        "ю": "yu",
        "я": "ya",
    },
}

EN_PREV_MAPPING = {"ье": "ye", "ъе": "ye"}
EN_NEXT_MAPPING = {"ье": "", "ъе": ""}

FR_MAPPING = {
    **BASE_MAPPING,
    **{
        "ё": "e",
        "ж": "j",
        "й": "i",
        "у": "ou",
        "х": "kh",
        "ц": "ts",
        "ч": "tch",
        "ш": "ch",
        "щ": "chtch",
        "ъ": "",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "iou",
        "я": "ia",
    },
}

FR_PREV_MAPPING = {"ге": "ue", "ги": "ui", "гы": "uy", "ье": "ie", "кс": "x"}
FR_NEXT_MAPPING = {"кс": ""}
FR_ENDING_MAPPING = {"ин": "ine"}

# Not implemented:
# `С` between two vowels → `SS` (Гусев → Goussev)

MVD_310 = Schema(EN_MAPPING, prev_mapping=EN_PREV_MAPPING, next_mapping=EN_NEXT_MAPPING)
MVD_310_FR = Schema(
    FR_MAPPING,
    prev_mapping=FR_PREV_MAPPING,
    next_mapping=FR_NEXT_MAPPING,
    ending_mapping=FR_ENDING_MAPPING,
)
