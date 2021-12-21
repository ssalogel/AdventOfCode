from src.AoC2015.Day2 import Day2
import pytest


@pytest.mark.parametrize("test_input,expected", [
    ('2x3x4', 58),
    ('1x1x10', 43)
])
def test_part1(test_input, expected):
    d = Day2(content="test")
    assert d.part1(d.parse_content(test_input)) == expected


@pytest.mark.parametrize("test_input,expected", [
    ('2x3x4', 34),
    ('1x1x10', 14)
])
def test_part2(test_input, expected):
    d = Day2(content="test")
    assert d.part2(d.parse_content(test_input)) == expected


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day2.txt', 'r') as file:
        content = file.read().strip()
    d = Day2(content="test")
    assert d.part1(d.parse_content(content)) == 1598415
    assert d.part2(d.parse_content(content)) == 3812909
