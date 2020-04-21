import pytest
import iuliia


@pytest.mark.parametrize(
    "source,expected",
    [
        ("Юлия Щеглова", "Yuliya Shcheglova"),
        ("Гайа Васильева", "Gaya Vasilyeva"),
        ("Андрей Видный", "Andrey Vidnyy"),
    ],
)
def test_mvd_310(source, expected):
    assert iuliia.translate(source, iuliia.MVD_310) == expected


@pytest.mark.parametrize(
    "source,expected",
    [
        ("Юлия Щеглова", "Iouliia Chtcheglova"),
        ("Гайа Васильева", "Gaia Vasilieva"),
        ("Андрей Видный", "Andrei Vidnyi"),
        ("Оксана Снегирёва", "Oxana Sneguireva"),
        ("Юрий Васин", "Iourii Vasine"),
    ],
)
def test_mvd_310_fr(source, expected):
    assert iuliia.translate(source, iuliia.MVD_310_FR) == expected
