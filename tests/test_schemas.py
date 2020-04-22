import iuliia


def test_schema_names():
    names = iuliia.Schemas.names()
    assert names == [
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
        "mvd_310",
        "mvd_310_fr",
        "mvd_782",
        "telegram",
        "wikipedia",
        "yandex_maps",
        "yandex_money",
    ]


def test_get_schema_by_name():
    schema = iuliia.Schemas.get("wikipedia")
    assert schema == iuliia.WIKIPEDIA
