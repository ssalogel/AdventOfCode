from src.AoC2016.Day10 import Day10


def test_actual_input():
    with open('./tests/aoc_2016/data/2016day10.txt', 'r') as file:
        content = file.read().strip()
    d = Day10(content="test")
    assert d.part1(d.parse_content(content)) == 98
    assert d.part2(d.parse_content(content)) == 4042
