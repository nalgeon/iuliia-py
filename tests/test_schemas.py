import pytest
import iuliia
from iuliia import Schema


def test_has():
    assert iuliia.schemas.has("wikipedia")
    assert not iuliia.schemas.has("unknown")


def test_get():
    schema = iuliia.schemas.get("wikipedia")
    assert schema.name == "wikipedia"
    with pytest.raises(ValueError):
        iuliia.schemas.get("unknown")


def test_schema_names():
    names = iuliia.schemas.names()
    assert names == [
        "ala_lc",
        "ala_lc_alt",
        "bgn_pcgn",
        "bgn_pcgn_alt",
        "bs_2979",
        "bs_2979_alt",
        "gost_16876",
        "gost_16876_alt",
        "gost_52290",
        "gost_52535",
        "gost_7034",
        "gost_779",
        "gost_779_alt",
        "icao_doc_9303",
        "iso_9_1954",
        "iso_9_1968",
        "iso_9_1968_alt",
        "mosmetro",
        "mvd_310",
        "mvd_310_fr",
        "mvd_782",
        "scientific",
        "telegram",
        "ungegn_1987",
        "uz",
        "wikipedia",
        "yandex_maps",
        "yandex_money",
    ]


def test_schema_items():
    items = iuliia.schemas.items()
    assert len(items) == 28
    assert items[0] == ("ala_lc", iuliia.schemas.get("ala_lc"))


def _sample_reader():
    for _, schema in iuliia.schemas.items():
        for source, expected in schema.samples:
            yield schema, source, expected


@pytest.mark.parametrize("schema,source,expected", _sample_reader())
def test_samples(schema: Schema, source: str, expected: str):
    assert schema.translate(source) == expected
