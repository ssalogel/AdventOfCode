from src.AoC2015.Day1 import Day1
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
    d = Day1(content="test")
    assert d.part1(d.parse_content(test_input)) == expected


@pytest.mark.parametrize("test_input,expected", [
    (")", 1),
    ("()())", 5)
])
def test_part2(test_input, expected):
    d = Day1(content="test")
    assert d.part2(d.parse_content(test_input)) == expected


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day1.txt', 'r') as file:
        content = file.read().strip()
    d = Day1(content="test")
    assert d.part1(d.parse_content(content)) == 232
    assert d.part2(d.parse_content(content)) == 1783
