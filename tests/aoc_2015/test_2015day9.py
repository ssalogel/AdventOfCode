from src.AoC2015.Day9 import Day9


def test_part1():
    content = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""
    d = Day9(content="test")
    assert d.part1(d.parse_content(content)) == 605


def test_part2():
    content = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""
    d = Day9(content="test")
    assert d.part2(d.parse_content(content)) == 982


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day9.txt', 'r') as file:
        content = file.read().strip()

    d = Day9(content="test")
    assert d.part1(d.parse_content(content)) == 207
    assert d.part2(d.parse_content(content)) == 804
