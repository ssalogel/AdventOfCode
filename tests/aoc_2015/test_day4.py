from AoC2015.Day4 import Day4
import pytest


@pytest.mark.parametrize("test_input,expected", [
    ("abcdef", 609043),
    ("pqrstuv", 1048970),

])
def test_find_hash(test_input, expected):
    assert Day4(content=test_input).find_hash(test_input, '00000') == expected
