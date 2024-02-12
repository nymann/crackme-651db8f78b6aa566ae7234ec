import pytest

from crackme_651db8f78b6aa566ae7234ec.key_generator import KeyGenerator
from crackme_651db8f78b6aa566ae7234ec.segment_generator import SegmentGenerator
from tests.unit_tests.crackme import crackme
from tests.unit_tests.crackme import segment_is_valid


def test_valid_key() -> None:
    keygen = KeyGenerator()
    key = keygen.generate()
    assert crackme(key)


@pytest.mark.parametrize("start", [x for x in range(360)])
def test_segment_generator(start: int) -> None:
    generator = SegmentGenerator(segment_length=4)
    segment = generator.generate(start)
    assert sum(ord(c) for c in segment) >= 10
    assert len(segment) == 4
    assert segment_is_valid(segment)
