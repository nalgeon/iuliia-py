import pytest
import iuliia


@pytest.mark.parametrize(
    "source,expected",
    [
        (
            "Россия, город Йошкар-Ола, улица Яна Крастыня",
            "Rossiya, gorod Yoshkar-Ola, ulitsa Yana Krastynya",
        ),
        ("Ельцин", "Yeltsin"),
        ("Раздольное", "Razdolnoye"),
        ("Юрьев", "Yuryev"),
        ("Белкин", "Belkin"),
        ("Бийск", "Biysk"),
        ("Подъярский", "Podyarsky"),
        ("Мусийкъонгийкоте", "Musiykyongiykote"),
        ("Давыдов", "Davydov"),
        ("Усолье", "Usolye"),
        ("Выхухоль", "Vykhukhol"),
        ("Дальнегорск", "Dalnegorsk"),
        ("Ильинский", "Ilyinsky"),
        ("Красный", "Krasny"),
        ("Великий", "Veliky"),
        ("Набережные Челны", "Naberezhnye Chelny"),
    ],
)
def test_wikipedia(source, expected):
    assert iuliia.translate(source, iuliia.WIKIPEDIA) == expected
