from AoC2015.Day1 import Day1
import pytest


@pytest.mark.parametrize("test_input,expected", [
    ("(())", 0),
    ("()()", 0),
    ("(((", 3),
    ("(()(()(", 3),
    ("))(((((", 3),
    ("())", -1),
    ("))(", -1),
    (")))", -3),
    (")())())", -3)
])
def test_part1(test_input, expected):
    assert Day1(content=test_input).part1() == expected


@pytest.mark.parametrize("test_input,expected", [
    (")", 1),
    ("()())", 5)
])
def test_part2(test_input, expected):
    assert Day1(content=test_input).part2() == expected


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day1.txt', 'r') as file:
        content = file.read().strip()
    assert Day1(content=content).part1() == 232
    assert Day1(content=content).part2() == 1783
