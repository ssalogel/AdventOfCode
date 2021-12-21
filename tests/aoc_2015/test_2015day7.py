from src.AoC2015.Day7 import Day7


def test_parse_content():
    content = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
"""
    d = Day7(content="test")
    assert d.parse_content(content=content) == [(('123',), 'x'), (('456',), 'y'), (('x', 'AND', 'y'), 'd'),
                                                (('x', 'OR', 'y'), 'e')]


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day7.txt', 'r') as file:
        content = file.read().strip()
    d = Day7(content="test")
    assert d.part1(d.parse_content(content)) == 956
    content.replace('14146', '956')
    assert d.part2(d.parse_content(content)) == 40149
