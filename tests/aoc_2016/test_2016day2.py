from src.AoC2016.Day2 import Day2


def test_part1():
    content = """ULL
RRDDD
LURDL
UUUUD"""
    d = Day2(content="test")
    assert d.part1(d.parse_content(content)) == "1985"


def test_part2():
    content = """ULL
RRDDD
LURDL
UUUUD"""
    d = Day2(content="test")
    assert d.part2(d.parse_content(content)) == '5DB3'


def test_actual_input():
    with open('./tests/aoc_2016/data/2016day2.txt', 'r') as file:
        content = file.read().strip()
    d = Day2(content="test")
    assert d.part1(d.parse_content(content)) == "82958"
    assert d.part2(d.parse_content(content)) == "B3DB8"
