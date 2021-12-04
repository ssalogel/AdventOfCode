from AoC2015.Day3 import Day3
import pytest


@pytest.mark.parametrize("test_input,expected", [
    (">", 2),
    ("^>v<", 4),
    ("^v^v^v^v^v", 2),

])
def test_part1(test_input, expected):
    d = Day3(content="test")
    assert d.part1(d.parse_content(test_input)) == expected


@pytest.mark.parametrize("test_input,expected", [
    ("^v", 3),
    ("^>v<", 3),
    ("^v^v^v^v^v", 11)
])
def test_part2(test_input, expected):
    d = Day3(content="test")
    assert d.part2(d.parse_content(test_input)) == expected


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day3.txt', 'r') as file:
        content = file.read().strip()
    d = Day3(content="test")
    assert d.part1(d.parse_content(content)) == 2081
    assert d.part2(d.parse_content(content)) == 2341
