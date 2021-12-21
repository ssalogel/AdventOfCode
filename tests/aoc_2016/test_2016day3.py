from src.AoC2016.Day3 import Day3


def test_actual_input():
    with open('./tests/aoc_2016/data/2016day3.txt', 'r') as file:
        content = file.read().strip()
    d = Day3(content="test")
    assert d.part1(d.parse_content(content)) == 1050
    assert d.part2(d.parse_content(content)) == 1921
