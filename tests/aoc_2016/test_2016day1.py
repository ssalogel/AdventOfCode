from AoC2016.Day1 import Day1
import pytest


@pytest.mark.parametrize("test_input,expected", [
    ("R2, L3", 5),
    ("R2, R2, R2", 2),
    ("R5, L5, R5, R3", 12)
])
def test_part1(test_input, expected):
    assert Day1(content=test_input).part1() == expected


def test_part2():
    assert Day1(content="R8, R4, R4, R8").part2() == 4


def test_actual_input():
    with open('./tests/aoc_2016/data/2016day1.txt', 'r') as file:
        content = file.read().strip()
    assert Day1(content=content).part1() == 291
    assert Day1(content=content).part2() == 159
