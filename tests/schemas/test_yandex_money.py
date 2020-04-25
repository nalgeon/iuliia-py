import pytest
import iuliia


@pytest.mark.parametrize(
    "source,expected",
    [
        (
            "Юлия, съешь ещё этих мягких французских булок из Йошкар-Олы, да выпей алтайского чаю",
            "Yuliya, sesh esche etikh myagkikh frantsuzskikh bulok iz Ioshkar-Oly, "
            "da vypei altaiskogo chayu",
        ),
        ("Юлия Щеглова", "Yuliya Scheglova"),
        ("Иван Брызгальский", "Ivan Bryzgalskii"),
        ("Ксения Стрый", "Kseniya Stryi"),
    ],
)
def test_yandex_money(source, expected):
    assert iuliia.translate(source, iuliia.YANDEX_MONEY) == expected
