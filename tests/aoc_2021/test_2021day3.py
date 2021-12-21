from src.AoC2021.Day3 import Day3


def test_part1():
    test_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
    d = Day3(content="test")
    assert d.part1(d.parse_content(test_input)) == 198


def test_part2():
    test_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
    d = Day3(content="test")
    assert d.part2(d.parse_content(test_input)) == 230


def test_actual_input():
    with open('./tests/aoc_2021/data/2021day3.txt', 'r') as file:
        content = file.read().strip()
    d = Day3(content="test")
    assert d.part1(d.parse_content(content)) == 3847100
    assert d.part2(d.parse_content(content)) == 4105235
