from AoC2015.Day25 import Day25


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day25.txt', 'r') as file:
        content = file.read().strip()
    d = Day25(content="test")
    assert d.part1(d.parse_content(content)) == 8997277
    assert d.part2(d.parse_content(content)) == "WINNER!"
