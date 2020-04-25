import pytest
import iuliia


@pytest.mark.parametrize(
    "source,expected",
    [
        (
            "Юлия, съешь ещё этих мягких французских булок из Йошкар-Олы, да выпей алтайского чаю",
            "Iuliia, sieesh eshche etikh miagkikh frantsuzskikh bulok iz Ioshkar-Oly, "
            "da vypei altaiskogo chaiu",
        ),
        ("Юлия Щеглова", "Iuliia Shcheglova"),
        ("Гайа Васильева", "Gaia Vasileva"),
        ("Андрей Видный", "Andrei Vidnyi"),
        ("Артём Краевой", "Artem Kraevoi"),
        ("Мадыр Чёткий", "Madyr Chetkii"),
        ("Оксана Клеёнкина", "Oksana Kleenkina"),
        ("Игорь Ильин", "Igor Ilin"),
        ("Ян Разъездной", "Ian Razieezdnoi"),
    ],
)
def test_icao_doc_9303(source, expected):
    assert iuliia.translate(source, iuliia.ICAO_DOC_9303) == expected
