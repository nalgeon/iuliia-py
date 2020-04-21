import pytest
import iuliia


@pytest.mark.parametrize(
    "source,expected",
    [
        ("Юлия Щеглова", "Yuliya Shcheglova"),
        ("Гайа Васильева", "Gaya Vasilyeva"),
        ("Андрей Видный", "Andrey Vidnyy"),
        ("Артём Краевой", "Artyem Krayevoy"),
        ("Мадыр Чёткий", "Madyr Chetkiy"),
        ("Оксана Клеёнкина", "Oksana Kleyonkina"),
        ("Игорь Ильин", "Igor' Ilyin"),
    ],
)
def test_mvd_782(source, expected):
    assert iuliia.translate(source, iuliia.MVD_782) == expected
