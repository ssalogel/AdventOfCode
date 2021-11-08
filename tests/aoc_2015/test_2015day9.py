from AoC2015.Day9 import Day9


def test_part1():
    content = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""
    assert Day9(content=content).part1() == 605


def test_part2():
    content = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""
    assert Day9(content=content).part2() == 982


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day9.txt', 'r') as file:
        content = file.read().strip()
    assert Day9(content=content).part1() == 207
    assert Day9(content=content).part2() == 804
