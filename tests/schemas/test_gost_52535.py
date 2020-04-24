import pytest
import iuliia


@pytest.mark.parametrize(
    "source,expected",
    [
        ("Юлия Щеглова", "Iuliia Shcheglova"),
        (
            "Юлия, съешь ещё этих мягких французских булок из Йошкар-Олы, да выпей алтайского чаю",
            "Iuliia, sesh eshche etikh miagkikh frantcuzskikh bulok iz Ioshkar-Oly, "
            "da vypei altaiskogo chaiu",
        ),
    ],
)
def test_gost_52535(source, expected):
    assert iuliia.translate(source, iuliia.GOST_52535) == expected
