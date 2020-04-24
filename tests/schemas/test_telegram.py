import pytest
import iuliia


@pytest.mark.parametrize(
    "source,expected",
    [
        (
            "Юлия, съешь ещё этих мягких французских булок из Йошкар-Олы, да выпей алтайского чаю",
            "Iuliia, sesh esce etih miagkih francuzskih bulok iz Ioshkar-Oly, "
            "da vypei altaiskogo chaiu",
        ),
    ],
)
def test_telegram(source, expected):
    assert iuliia.translate(source, iuliia.TELEGRAM) == expected
