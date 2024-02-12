from tests.unit_tests.crackme import crackme


def test_valid_key_is_valid() -> None:
    assert crackme("!!!&-!!!(-!!!2-!!!4")


def test_invalid_key() -> None:
    assert not crackme("!!!(-!!!&-!!!2-!!!4")
