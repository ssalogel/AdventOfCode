from src.AoC2015.Day20 import Day20
import pytest


@pytest.mark.parametrize("test_input,expected", [
    ('150', 8),
    ('10', 1),
    ('120', 6)
])
def test_part1(test_input, expected):
    d = Day20(content="test")
    assert d.part1(d.parse_content(test_input)) == expected


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day20.txt', 'r') as file:
        content = file.read().strip()
    d = Day20(content="test")
    assert d.part1(d.parse_content(content)) == 786240
    assert d.part2(d.parse_content(content)) == 831600
