import pytest
import iuliia


@pytest.mark.parametrize(
    "source,expected",
    [
        (
            "Юлия, съешь ещё этих мягких французских булок из Йошкар-Олы, да выпей алтайского чаю",
            'Julija, s"ešʹ eščë ėtih mjagkih francuzskih bulok iz Joškar-Oly, '
            "da vypej altajskogo čaju",
        ),
    ],
)
def test_iso_9_1954(source, expected):
    assert iuliia.translate(source, iuliia.ISO_9_1954) == expected
