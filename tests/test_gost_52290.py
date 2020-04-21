import pytest
import iuliia


@pytest.mark.parametrize(
    "source,expected",
    [
        (
            "Россия, город Йошкар-Ола, улица Яна Крастыня",
            "Rossiya, gorod Yoshkar-Ola, ulitsa Yana Krastynya",
        ),
        (
            "Юлия, съешь ещё этих мягких французских булок из Йошкар-Олы, да выпей алтайского чаю",
            "Yuliya, syesh' eshche etikh myagkikh frantsuzskikh bulok iz Yoshkar-Oly, "
            "da vypey altayskogo chayu",
        ),
        ("Ё Крё Мякоё", "Yo Krye Myakoyo"),
    ],
)
def test_gost_52290(source, expected):
    assert iuliia.translate(source, iuliia.GOST_52290) == expected
