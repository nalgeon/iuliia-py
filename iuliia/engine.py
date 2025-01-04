"""
Translate engine (deprecated).
"""

import warnings
from .schema import Schema


def translate(source: str, schema: Schema) -> str:
    """
    Translate the Cyrillic string into Latin using the provided schema.
    Delegates transliteration specifics to the schema.
    DEPRECATED: Use schema.translate() instead.
    """
    warnings.warn(
        "The 'translate' function is deprecated. Use schema.translate() instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return schema.translate(source)
