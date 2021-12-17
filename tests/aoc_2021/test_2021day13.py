from AoC2021.Day13 import Day13


def test_part1():
    test_input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""
    d = Day13(content="test")
    assert d.part1(d.parse_content(test_input)) == 17


def test_actual_input():
    with open('./tests/aoc_2021/data/2021day13.txt', 'r') as file:
        content = file.read().strip()
    d = Day13(content="test")
    assert d.part1(d.parse_content(content)) == 775
