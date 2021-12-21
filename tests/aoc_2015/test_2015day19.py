from src.AoC2015.Day19 import Day19


def test_part1():
    content = """H => HO
H => OH
O => HH

HOH"""
    d = Day19(content="test")
    assert d.part1(d.parse_content(content)) == 4


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day19.txt', 'r') as file:
        content = file.read().strip()
    d = Day19(content="test")
    assert d.part1(d.parse_content(content)) == 576
    assert d.part2(d.parse_content(content)) == 207
