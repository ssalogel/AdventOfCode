from src.AoC2015.Day23 import Day23


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day23.txt', 'r') as file:
        content = file.read().strip()
    d = Day23(content="test")
    assert d.part1(d.parse_content(content)) == 307
    assert d.part2(d.parse_content(content)) == 160
