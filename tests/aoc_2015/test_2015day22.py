from src.AoC2015.Day22 import Day22


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day22.txt', 'r') as file:
        content = file.read().strip()
    d = Day22(content="test")
    assert d.part1(d.parse_content(content)) == 953
    assert d.part2(d.parse_content(content)) == 1289
