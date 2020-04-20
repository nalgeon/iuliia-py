"""
Wikipedia transliteration schema.
https://dangry.ru/iuliia/wikipedia/
"""

from .schema import Schema

MAPPING = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "yo",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "y",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "kh",
    "ц": "ts",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "ъ": "",
    "ы": "y",
    "ь": "",
    "э": "e",
    "ю": "yu",
    "я": "ya",
}

PREV_MAPPING = {
    "е": "ye",
    "ае": "ye",
    "ие": "ye",
    "ое": "ye",
    "уе": "ye",
    "эе": "ye",
    "юе": "ye",
    "яе": "ye",
    "ье": "ye",
    "ъе": "ye",
}

NEXT_MAPPING = {
    "ъа": "y",
    "ъи": "y",
    "ъо": "y",
    "ъу": "y",
    "ъы": "y",
    "ъэ": "y",
    "ьа": "y",
    "ьи": "y",
    "ьо": "y",
    "ьу": "y",
    "ьы": "y",
    "ьэ": "y",
}

ENDING_MAPPING = {
    "ий": "y",
    "ый": "y",
}

WIKIPEDIA = Schema(
    MAPPING, prev_mapping=PREV_MAPPING, next_mapping=NEXT_MAPPING, ending_mapping=ENDING_MAPPING,
)
