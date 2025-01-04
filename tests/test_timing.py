import os
import timeit
import pytest
import iuliia


@pytest.mark.skipif(
    os.getenv("TEST_TIMING") is None, reason="skip timing test until explicitly requested"
)
def test_timing():
    source = "Юлия, съешь ещё этих мягких французских булок из Йошкар-Олы, да выпей алтайского чаю"
    iter_count = 10000
    max_sec = 1.0
    print(f"#iterations={iter_count}")
    for schema in [iuliia.GOST_779, iuliia.ICAO_DOC_9303, iuliia.MOSMETRO, iuliia.WIKIPEDIA]:
        elapsed_sec = timeit.timeit(lambda: schema.translate(source), number=10000)
        print(f"{schema.name}: elapsed={elapsed_sec:.3f} sec")
        assert elapsed_sec < max_sec
