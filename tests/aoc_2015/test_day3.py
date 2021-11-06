from AoC2015.Day3 import Day3
import pytest


@pytest.mark.parametrize("test_input,expected", [
    (">", 2),
    ("^>v<", 4),
    ("^v^v^v^v^v", 2),

])
def test_part1(test_input, expected):
    assert Day3(content=test_input).part1() == expected


@pytest.mark.parametrize("test_input,expected", [
    ("^v", 3),
    ("^>v<", 3),
    ("^v^v^v^v^v", 11)
])
def test_part2(test_input, expected):
    assert Day3(content=test_input).part2() == expected


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day3.txt', 'r') as file:
        content = file.read().strip()
    assert Day3(content=content).part1() == 2081
    assert Day3(content=content).part2() == 2341
