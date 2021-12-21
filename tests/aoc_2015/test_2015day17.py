from src.AoC2015.Day17 import Day17


def test_part1():
    content = """20
15
10
5
5"""
    d = Day17(content="test", target=25)
    assert d.part1(d.parse_content(content=content)) == 4


def test_part2():
    content = """20
15
10
5
5"""
    d = Day17(content="test", target=25)
    assert d.part2(d.parse_content(content=content)) == 3


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day17.txt', 'r') as file:
        content = file.read().strip()
    d = Day17(content="test")
    assert d.part1(d.parse_content(content)) == 654
    assert d.part2(d.parse_content(content)) == 57
