import pytest
import iuliia


@pytest.mark.parametrize(
    "source,expected",
    [
        (
            "Юлия, съешь ещё этих мягких французских булок из Йошкар-Олы, да выпей алтайского чаю",
            "Julija, sʺešʹ eščё ètix mjagkix francuzskix bulok iz Joškar-Oly, "
            "da vypej altajskogo čaju",
        ),
    ],
)
def test_scientific(source, expected):
    assert iuliia.translate(source, iuliia.SCIENTIFIC) == expected
