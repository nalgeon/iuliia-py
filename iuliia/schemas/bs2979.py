"""
British Standard 2979:1958 transliteration schema.
https://dangry.ru/iuliia/bs-2979/
"""

from iuliia.mapping import BASE_MAPPING
from iuliia.schema import Schema

MAPPING = {
    **BASE_MAPPING,
    **{
        "ё": "ё",
        "ж": "zh",
        "й": "ĭ",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": "ʺ",
        # This schema defines two alternative translations for `Ы`:
        #   - `Ы` → `Ȳ` (used by the Oxford University Press)
        #   - `Ы` → `UI` (used by the British Library).
        # `iuliia` uses `Ы` → `Ȳ`.
        "ы": "ȳ",
        "ь": "ʹ",
        "э": "é",
        "ю": "yu",
        "я": "ya",
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
        "ю": "yu",
        "я": "ya",
    },
}

ENDING_MAPPING = {"ий": "y", "ый": "y"}

BS_2979 = Schema(MAPPING, ending_mapping=ENDING_MAPPING)
BS_2979_ALT = Schema(ALT_MAPPING, ending_mapping=ENDING_MAPPING)
