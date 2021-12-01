from AoC2016.Day2 import Day2


def test_part1():
    content = """ULL
RRDDD
LURDL
UUUUD"""
    assert Day2(content=content).part1() == "1985"


def test_part2():
    content = """ULL
RRDDD
LURDL
UUUUD"""
    assert Day2(content=content).part2() == '5DB3'


def test_actual_input():
    with open('./tests/aoc_2016/data/2016day2.txt', 'r') as file:
        content = file.read().strip()
    assert Day2(content=content).part1() == "82958"
    assert Day2(content=content).part2() == "B3DB8"
