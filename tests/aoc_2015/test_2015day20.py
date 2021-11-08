from AoC2015.Day20 import Day20
import pytest


@pytest.mark.parametrize("test_input,expected", [
    ('150', 8),
    ('10', 1),
    ('120', 6)
])
def test_part1(test_input, expected):
    assert Day20(content=test_input).part1() == expected


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day20.txt', 'r') as file:
        content = file.read().strip()
    assert Day20(content=content).part1() == 786240
    assert Day20(content=content).part2() == 831600
