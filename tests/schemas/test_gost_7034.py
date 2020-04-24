import pytest
import iuliia


@pytest.mark.parametrize(
    "source,expected",
    [
        (
            "Юлия, съешь ещё этих мягких французских булок из Йошкар-Олы, да выпей алтайского чаю",
            "Yuliya, s''esh' eshhyo etix myagkix francuzskix bulok iz Joshkar-Oly, "
            "da vypej altajskogo chayu",
        ),
    ],
)
def test_gost_7034(source, expected):
    assert iuliia.translate(source, iuliia.GOST_7034) == expected
