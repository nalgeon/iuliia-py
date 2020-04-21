import pytest
import iuliia


@pytest.mark.parametrize(
    "source,expected",
    [
        (
            "Россия, город Йошкар-Ола, улица Яна Крастыня",
            "Rossiya, gorod Yoshkar-Ola, ulitsa Yana Krastynya",
        ),
        ("Санкт-Петербург, Подъездной пер", "Sankt-Peterburg, Podyezdnoy per"),
        ("Москва, ул Подъёмная", "Moskva, ul Podyomnaya"),
        ("Астрахань, ул Подъяпольского", "Astrakhan, ul Podyapolskogo"),
        ("Щегловитовка", "Scheglovitovka"),
        ("Новый Уренгой", "Noviy Urengoy"),
    ],
)
def test_yandex_maps(source, expected):
    assert iuliia.translate(source, iuliia.YANDEX_MAPS) == expected
