from AoC2015.Day17 import Day17


def test_part1():
    content = """20
15
10
5
5"""
    assert Day17(content=content, target=25).part1() == 4


def test_part2():
    content = """20
15
10
5
5"""
    assert Day17(content=content, target=25).part2() == 3


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day17.txt', 'r') as file:
        content = file.read().strip()
    assert Day17(content=content).part1() == 654
    assert Day17(content=content).part2() == 57
