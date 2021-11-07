from AoC2015.Day20 import Day20
import pytest


@pytest.mark.parametrize("test_input,expected", [
    ('150', 8),
    ('10', 1),
    ('120', 6)
])
def test_part1(test_input, expected):
    assert Day20(content=test_input).part1() == expected
