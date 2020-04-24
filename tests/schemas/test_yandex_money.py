import pytest
import iuliia


@pytest.mark.parametrize(
    "source,expected",
    [
        ("Юлия Щеглова", "Yuliya Scheglova"),
        ("Иван Брызгальский", "Ivan Bryzgalskii"),
        ("Ксения Стрый", "Kseniya Stryi"),
    ],
)
def test_yandex_money(source, expected):
    assert iuliia.translate(source, iuliia.YANDEX_MONEY) == expected
