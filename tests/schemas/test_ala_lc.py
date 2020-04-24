import pytest
import iuliia


@pytest.mark.parametrize(
    "source,expected",
    [
        (
            "Юлия, съешь ещё этих мягких французских булок из Йошкар-Олы, да выпей алтайского чаю",
            "I͡ulii͡a, sʺeshʹ eshchё ėtikh mi͡agkikh frant͡suzskikh bulok iz Ĭoshkar-Oly, "
            "da vypeĭ altaĭskogo chai͡u",
        ),
    ],
)
def test_ala_lc(source, expected):
    assert iuliia.translate(source, iuliia.ALA_LC) == expected


@pytest.mark.parametrize(
    "source,expected",
    [
        (
            "Юлия, съешь ещё этих мягких французских булок из Йошкар-Олы, да выпей алтайского чаю",
            "Iuliia, s\"esh' eshche etikh miagkikh frantsuzskikh bulok iz Ioshkar-Oly, "
            "da vypei altaiskogo chaiu",
        ),
    ],
)
def test_ala_lc_alt(source, expected):
    assert iuliia.translate(source, iuliia.ALA_LC_ALT) == expected
