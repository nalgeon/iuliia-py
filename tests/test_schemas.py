import pytest
from iuliia import Schemas


def test_schema_names():
    names = Schemas.names()
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
    items = Schemas.items()
    assert len(items) == 28
    assert items[0] == ("ala_lc", Schemas.get("ala_lc"))


def test_get():
    schema = Schemas.get("wikipedia")
    assert schema.name == "wikipedia"

    with pytest.raises(ValueError) as exc:
        Schemas.get("invalid")
    assert str(exc.value) == "Schema 'invalid' does not exist"


def _sample_reader():
    for _, schema in Schemas.items():
        for source, expected in schema.samples:
            yield schema, source, expected


@pytest.mark.parametrize("schema,source,expected", _sample_reader())
def test_samples(schema, source, expected):
    assert schema.translate(source) == expected
