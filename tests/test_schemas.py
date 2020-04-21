import pytest
import iuliia


def test_schema_names():
    names = iuliia.Schemas.names()
    assert names == ["wikipedia", "yandex_maps", "yandex_money"]


def test_get_schema_by_name():
    schema = iuliia.Schemas.get("wikipedia")
    assert schema == iuliia.WIKIPEDIA


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
