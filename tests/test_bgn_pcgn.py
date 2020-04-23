import pytest
import iuliia


@pytest.mark.parametrize(
    "source,expected",
    [
        (
            "Юлия, съешь ещё этих мягких французских булок из Йошкар-Олы, да выпей алтайского чаю",
            "Yuliya, s”yesh’ yeshchё etikh myagkikh frantsuzskikh bulok iz Yoshkar-Oly, "
            "da vypey altayskogo chayu",
        ),
        (
            "Россия, город Йошкар-Ола, улица Яна Крастыня",
            "Rossiya, gorod Yoshkar-Ola, ulitsa Yana Krastynya",
        ),
        ("Елизово", "Yelizovo"),
        ("Чапаевск", "Chapayevsk"),
        ("Мейеровка", "Meyyerovka"),
        ("Юрьев объезд", "Yur’yev ob”yezd"),
        ("Белкино", "Belkino"),
        ("Ёдва", "Yёdva"),
        ("Змииёвка", "Zmiiyёvka"),
        ("Айёган", "Ayyёgan"),
        ("Воробьёво", "Vorob’yёvo"),
        ("Кебанъёль", "Keban”yёl’"),
        ("Озёрный", "Ozёrnyy"),
        ("Тыайа", "Ty·ay·a"),
        ("Сайылык", "Say·ylyk"),
        ("Ойусардах", "Oy·usardakh"),
        ("Йошкар-Ола", "Yoshkar-Ola"),
        ("Бийск", "Biysk"),
        ("Тыэкан", "Ty·ekan"),
        ("Суык-Су", "Su·yk-Su"),
        ("Тында", "Tynda"),
        ("Улан-Удэ", "Ulan-Ud·e"),
        ("Электрогорск", "Elektrogorsk"),
        ("Руэм", "Ruem"),
        ("Вяртсиля", "Vyart·silya"),
        ("Ташчишма", "Tash·chishma"),
    ],
)
def test_bgn_pcgn(source, expected):
    assert iuliia.translate(source, iuliia.BGN_PCGN) == expected


@pytest.mark.parametrize(
    "source,expected",
    [
        (
            "Юлия, съешь ещё этих мягких французских булок из Йошкар-Олы, да выпей алтайского чаю",
            "Yuliya, s”yesh’ yeshchё etikh myagkikh frantsuzskikh bulok iz Yoshkar-Oly, "
            "da vypey altayskogo chayu",
        ),
        (
            "Россия, город Йошкар-Ола, улица Яна Крастыня",
            "Rossiya, gorod Yoshkar-Ola, ulitsa Yana Krastynya",
        ),
        ("Елизово", "Yelizovo"),
        ("Чапаевск", "Chapayevsk"),
        ("Мейеровка", "Meyyerovka"),
        ("Юрьев объезд", "Yur’yev ob”yezd"),
        ("Белкино", "Belkino"),
        ("Ёдва", "Yёdva"),
        ("Змииёвка", "Zmiiyёvka"),
        ("Айёган", "Ayyёgan"),
        ("Воробьёво", "Vorob’yёvo"),
        ("Кебанъёль", "Keban”yёl’"),
        ("Озёрный", "Ozёrnyy"),
        ("Тыайа", "Tyaya"),
        ("Сайылык", "Sayylyk"),
        ("Ойусардах", "Oyusardakh"),
        ("Йошкар-Ола", "Yoshkar-Ola"),
        ("Бийск", "Biysk"),
        ("Тыэкан", "Tyekan"),
        ("Суык-Су", "Suyk-Su"),
        ("Тында", "Tynda"),
        ("Улан-Удэ", "Ulan-Ude"),
        ("Электрогорск", "Elektrogorsk"),
        ("Руэм", "Ruem"),
        ("Вяртсиля", "Vyartsilya"),
        ("Ташчишма", "Tashchishma"),
    ],
)
def test_bgn_pcgn_alt(source, expected):
    assert iuliia.translate(source, iuliia.BGN_PCGN_ALT) == expected
