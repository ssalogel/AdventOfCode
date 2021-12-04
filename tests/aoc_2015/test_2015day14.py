from AoC2015.Day14 import Day14


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day14.txt', 'r') as file:
        content = file.read().strip()
    d = Day14(content="test")
    assert d.part1(d.parse_content(content)) == 2655
    assert d.part2(d.parse_content(content)) == 1059
