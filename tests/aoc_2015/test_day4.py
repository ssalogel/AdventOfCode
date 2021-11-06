from AoC2015.Day4 import Day4
import pytest


@pytest.mark.parametrize("test_input,expected", [
    ("abcdef", 609043),
    ("pqrstuv", 1048970),

])
def test_part1(test_input, expected):
    assert Day4(content=test_input).part1() == expected


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day4.txt', 'r') as file:
        content = file.read().strip()
    assert Day4(content=content).part1() == 346386
    assert Day4(content=content).part2() == 9958218
