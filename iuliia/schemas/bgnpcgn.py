"""
BGN/PCGN transliteration schema.
https://dangry.ru/iuliia/bgn-pcgn/
"""

from iuliia.mapping import BASE_MAPPING
from iuliia.schema import Schema

MAPPING = {
    **BASE_MAPPING,
    **{
        "ё": "ё",
        "ж": "zh",
        "й": "y",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": "”",
        "ы": "y",
        "ь": "’",
        "э": "e",
        "ю": "yu",
        "я": "ya",
    },
}

PREV_MAPPING_ALT = {
    # е
    "е": "ye",
    "ае": "ye",
    "ее": "ye",
    "ёе": "ye",
    "ие": "ye",
    "йе": "ye",
    "ое": "ye",
    "уе": "ye",
    "ъе": "ye",
    "ые": "ye",
    "ье": "ye",
    "эе": "ye",
    "юе": "ye",
    "яе": "ye",
    # ё
    "ё": "yё",
    "аё": "yё",
    "её": "yё",
    "ёё": "yё",
    "иё": "yё",
    "йё": "yё",
    "оё": "yё",
    "уё": "yё",
    "ъё": "yё",
    "ыё": "yё",
    "ьё": "yё",
    "эё": "yё",
    "юё": "yё",
    "яё": "yё",
}

PREV_MAPPING = {
    **PREV_MAPPING_ALT,
    **{
        # ы
        "аы": "·y",
        "еы": "·y",
        "ёы": "·y",
        "иы": "·y",
        "оы": "·y",
        "уы": "·y",
        "ыы": "·y",
        "эы": "·y",
        "юы": "·y",
        "яы": "·y",
        # э
        "бэ": "·e",
        "вэ": "·e",
        "гэ": "·e",
        "дэ": "·e",
        "жэ": "·e",
        "зэ": "·e",
        "кэ": "·e",
        "лэ": "·e",
        "мэ": "·e",
        "нэ": "·e",
        "пэ": "·e",
        "рэ": "·e",
        "сэ": "·e",
        "тэ": "·e",
        "фэ": "·e",
        "хэ": "·e",
        "цэ": "·e",
        "чэ": "·e",
        "шэ": "·e",
        "щэ": "·e",
    },
}

NEXT_MAPPING = {
    "йа": "y·",
    "йу": "y·",
    "йы": "y·",
    "йэ": "y·",
    "ыа": "y·",
    "ыу": "y·",
    "ыы": "y·",
    "ыэ": "y·",
    "тс": "t·",
    "шч": "sh·",
}

BGN_PCGN = Schema(MAPPING, prev_mapping=PREV_MAPPING, next_mapping=NEXT_MAPPING)
BGN_PCGN_ALT = Schema(MAPPING, prev_mapping=PREV_MAPPING_ALT)
