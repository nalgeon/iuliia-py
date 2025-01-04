"""
Schema registry.
"""

from enum import Enum
import operator
from .lazy import LazySchema
from .schema import Schema


# pylint: disable=invalid-name
class Schemas(Enum):
    """
    All supported transliteration schemas.
    """

    ala_lc = LazySchema("ala_lc")
    ala_lc_alt = LazySchema("ala_lc_alt")
    bgn_pcgn = LazySchema("bgn_pcgn")
    bgn_pcgn_alt = LazySchema("bgn_pcgn_alt")
    bs_2979 = LazySchema("bs_2979")
    bs_2979_alt = LazySchema("bs_2979_alt")
    gost_16876 = LazySchema("gost_16876")
    gost_16876_alt = LazySchema("gost_16876_alt")
    gost_52290 = LazySchema("gost_52290")
    gost_52535 = LazySchema("gost_52535")
    gost_7034 = LazySchema("gost_7034")
    gost_779 = LazySchema("gost_779")
    gost_779_alt = LazySchema("gost_779_alt")
    icao_doc_9303 = LazySchema("icao_doc_9303")
    iso_9_1954 = LazySchema("iso_9_1954")
    iso_9_1968 = LazySchema("iso_9_1968")
    iso_9_1968_alt = LazySchema("iso_9_1968_alt")
    mosmetro = LazySchema("mosmetro")
    mvd_310 = LazySchema("mvd_310")
    mvd_310_fr = LazySchema("mvd_310_fr")
    mvd_782 = LazySchema("mvd_782")
    scientific = LazySchema("scientific")
    telegram = LazySchema("telegram")
    ungegn_1987 = LazySchema("ungegn_1987")
    uz = LazySchema("uz")
    wikipedia = LazySchema("wikipedia")
    yandex_maps = LazySchema("yandex_maps")
    yandex_money = LazySchema("yandex_money")

    @classmethod
    def names(cls) -> list[str]:
        """Return names of all supported schemas."""
        return sorted(item.name for item in cls)

    @classmethod
    def items(cls) -> list[tuple[str, Schema]]:
        """Return all supported schemas."""
        return [
            (item.name, item.value) for item in sorted(cls, key=operator.attrgetter("value.name"))
        ]

    @classmethod
    def get(cls, name: str) -> Schema:
        """
        Return schema by its name.
        Raises ValueError if schema does not exist.
        """
        item = cls.__members__.get(name)
        if not item:
            raise ValueError(f"Schema '{name}' does not exist")
        return item.value
