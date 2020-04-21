import pytest
import iuliia


@pytest.mark.parametrize(
    "source,expected",
    [
        (
            "Юлия, съешь ещё этих мягких французских булок из Йошкар-Олы, да выпей алтайского чаю",
            "Ûliâ, sʺešʹ eŝё ètih mâgkih francuzskih bulok iz Joškar-Oly, da vypej altajskogo čaû",
        ),
    ],
)
def test_gost_779(source, expected):
    assert iuliia.translate(source, iuliia.GOST_779) == expected


@pytest.mark.parametrize(
    "source,expected",
    [
        (
            "Юлия, съешь ещё этих мягких французских булок из Йошкар-Олы, да выпей алтайского чаю",
            "Yuliya, s``esh` eshhyo е`tix myagkix franczuzskix bulok iz Joshkar-Oly`, "
            "da vy`pej altajskogo chayu",
        ),
    ],
)
def test_gost_779_alt(source, expected):
    assert iuliia.translate(source, iuliia.GOST_779_ALT) == expected
