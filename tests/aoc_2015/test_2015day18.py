from src.AoC2015.Day18 import Day18


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day18.txt', 'r') as file:
        content = file.read().strip()
    d = Day18(content="test")
    assert d.part1(d.parse_content(content)) == 1061
    assert d.part2(d.parse_content(content)) == 1006
