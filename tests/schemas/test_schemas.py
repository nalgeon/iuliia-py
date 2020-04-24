import iuliia


def test_schema_names():
    names = iuliia.Schemas.names()
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
        "mvd_310",
        "mvd_310_fr",
        "mvd_782",
        "scientific",
        "telegram",
        "ungegn_1987",
        "wikipedia",
        "yandex_maps",
        "yandex_money",
    ]


def test_get_schema_by_name():
    schema = iuliia.Schemas.get("wikipedia")
    assert schema == iuliia.WIKIPEDIA
