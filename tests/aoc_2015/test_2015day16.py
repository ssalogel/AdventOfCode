from AoC2015.Day16 import Day16


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day16.txt', 'r') as file:
        content = file.read().strip()
    d = Day16(content="test")
    assert d.part1(d.parse_content(content)) == '103'
    assert d.part2(d.parse_content(content)) == '405'
