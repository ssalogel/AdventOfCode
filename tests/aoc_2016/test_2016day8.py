from AoC2016.Day8 import Day8


def test_part1():
    content = """rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1"""
    d = Day8(content="test")
    assert d.part1(d.parse_content(content)) == 6


def test_actual_input():
    with open('./tests/aoc_2016/data/2016day8.txt', 'r') as file:
        content = file.read().strip()
    d = Day8(content="test")
    assert d.part1(d.parse_content(content)) == 106
