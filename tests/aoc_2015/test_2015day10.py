from src.AoC2015.Day10 import Day10
import pytest


@pytest.mark.parametrize("test_input,expected", [
    ("1", "11"),
    ("11", "21"),
    ("1211", "111221"),
    ("111221", "312211"),
])
def test_step(test_input, expected):
    assert Day10(content='test').step(test_input) == expected
