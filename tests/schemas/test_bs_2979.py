import pytest
import iuliia


@pytest.mark.parametrize(
    "source,expected",
    [
        (
            "Юлия, съешь ещё этих мягких французских булок из Йошкар-Олы, да выпей алтайского чаю",
            "Yuliya, sʺeshʹ eshchё étikh myagkikh frantsuzskikh bulok iz Ĭoshkar-Olȳ, "
            "da vȳpeĭ altaĭskogo chayu",
        ),
    ],
)
def test_bs_2979(source, expected):
    assert iuliia.translate(source, iuliia.BS_2979) == expected


@pytest.mark.parametrize(
    "source,expected",
    [
        (
            "Юлия, съешь ещё этих мягких французских булок из Йошкар-Олы, да выпей алтайского чаю",
            "Yuliya, s\"esh' eshche etikh myagkikh frantsuzskikh bulok iz Ioshkar-Oly, "
            "da vypei altaiskogo chayu",
        ),
    ],
)
def test_bs_2979_alt(source, expected):
    assert iuliia.translate(source, iuliia.BS_2979_ALT) == expected
