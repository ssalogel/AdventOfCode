from AoC2015.Day7 import Day7


def test_parse_content():
    content = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
"""
    print(Day7(content=content).parse_content())
    assert Day7(content=content).parse_content() == [(('123',), 'x'), (('456',), 'y'), (('x', 'AND', 'y'), 'd'),
                                                     (('x', 'OR', 'y'), 'e')]


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day7.txt', 'r') as file:
        content = file.read().strip()
    assert Day7(content=content).part1() == 956
    content.replace('14146', '956')
    assert Day7(content=content).part2() == 40149
