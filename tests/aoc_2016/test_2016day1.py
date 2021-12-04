from AoC2016.Day1 import Day1
import pytest


@pytest.mark.parametrize("test_input,expected", [
    ("R2, L3", 5),
    ("R2, R2, R2", 2),
    ("R5, L5, R5, R3", 12)
])
def test_part1(test_input, expected):
    d = Day1(content="test")
    assert d.part1(d.parse_content(test_input)) == expected


def test_part2():
    d = Day1(content="test")
    assert d.part2(d.parse_content(content="R8, R4, R4, R8")) == 4


def test_actual_input():
    with open('./tests/aoc_2016/data/2016day1.txt', 'r') as file:
        content = file.read().strip()
    d = Day1(content="test")
    assert d.part1(d.parse_content(content)) == 291
    assert d.part2(d.parse_content(content)) == 159
