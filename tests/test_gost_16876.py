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
def test_gost_16876(source, expected):
    assert iuliia.translate(source, iuliia.GOST_16876) == expected


@pytest.mark.parametrize(
    "source,expected",
    [
        (
            "Юлия, съешь ещё этих мягких французских булок из Йошкар-Олы, да выпей алтайского чаю",
            "Julija, s\"esh' eshhjo ehtikh mjagkikh francuzskikh bulok iz Jjoshkar-Oly, "
            "da vypejj altajjskogo chaju",
        ),
    ],
)
def test_gost_16876_alt(source, expected):
    assert iuliia.translate(source, iuliia.GOST_16876_ALT) == expected
