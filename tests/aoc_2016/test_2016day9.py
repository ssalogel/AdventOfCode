from src.AoC2016.Day9 import Day9
import pytest


@pytest.mark.parametrize("test_input,expected", [
    ("ADVENT", 6),
    ("A(1x5)BC", 7),
    ("(3x3)XYZ", 9),
    ("A(2x2)BCD(2x2)EFG", 11),
    ("(6x1)(1x3)A", 6),
    ("X(8x2)(3x3)ABCY", 18)
])
def test_part1(test_input, expected):
    d = Day9(content="test")
    assert d.part1(d.parse_content(test_input)) == expected


@pytest.mark.parametrize("test_input,expected", [
    ("X(8x2)(3x3)ABCY", 20),
    ("(27x12)(20x12)(13x14)(7x10)(1x12)A", 241920),
    ("(3x3)XYZ", 9),
    ("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 445),
])
def test_part2(test_input, expected):
    d = Day9(content="test")
    assert d.part2(d.parse_content(test_input)) == expected


def test_actual_input():
    with open('./tests/aoc_2016/data/2016day9.txt', 'r') as file:
        content = file.read().strip()
    d = Day9(content="test")
    assert d.part1(d.parse_content(content)) == 120765
    assert d.part2(d.parse_content(content)) == 11658395076
