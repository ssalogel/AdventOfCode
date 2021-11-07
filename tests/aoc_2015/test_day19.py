from AoC2015.Day19 import Day19


def test_part1():
    content = """H => HO
H => OH
O => HH

HOH"""
    assert Day19(content=content).part1() == 4


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day19.txt', 'r') as file:
        content = file.read().strip()
    assert Day19(content=content).part1() == 576
    assert Day19(content=content).part2() == 207
