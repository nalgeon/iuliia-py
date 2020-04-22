import pytest
import iuliia


@pytest.mark.parametrize(
    "source,expected",
    [
        (
            "Юлия, съешь ещё этих мягких французских булок из Йошкар-Олы, да выпей алтайского чаю",
            "Julija, sʺešʹ eščë ėtih mjagkih francuzskih bulok iz Joškar-Oly, "
            "da vypej altajskogo čaju",
        ),
    ],
)
def test_iso_9_1968(source, expected):
    assert iuliia.translate(source, iuliia.ISO_9_1968) == expected


@pytest.mark.parametrize(
    "source,expected",
    [
        (
            "Юлия, съешь ещё этих мягких французских булок из Йошкар-Олы, да выпей алтайского чаю",
            "Yulyya, sʺeshʹ eshchë ėtykh myagkykh frantsuzskykh bulok yz Ĭoshkar-Oly, "
            "da vypeĭ altaĭskogo chayu",
        ),
    ],
)
def test_iso_9_1968_alt(source, expected):
    assert iuliia.translate(source, iuliia.ISO_9_1968_ALT) == expected
