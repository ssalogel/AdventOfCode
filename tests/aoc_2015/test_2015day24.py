from AoC2015.Day24 import Day24


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day24.txt', 'r') as file:
        content = file.read().strip()
    d = Day24(content="test")
    assert d.part1(d.parse_content(content)) == 10723906903
    assert d.part2(d.parse_content(content)) == 74850409
