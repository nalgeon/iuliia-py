import pytest
import iuliia


@pytest.mark.parametrize(
    "source,expected",
    [
        (
            "Юлия, съешь ещё этих мягких французских булок из Йошкар-Олы, да выпей алтайского чаю",
            "Julija, sʺešʹ eščё ètih mjagkih francuzskih bulok iz Joškar-Oly, "
            "da vypej altajskogo čaju",
        ),
        (
            "Россия, город Йошкар-Ола, улица Яна Крастыня",
            "Rossija, gorod Joškar-Ola, ulica Jana Krastynja",
        ),
    ],
)
def test_ungegn_1987(source, expected):
    assert iuliia.translate(source, iuliia.UNGEGN_1987) == expected
