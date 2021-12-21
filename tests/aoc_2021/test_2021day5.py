from src.AoC2021.Day5 import Day5


def test_part1():
    test_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
    d = Day5(content="test")
    assert d.part1(d.parse_content(test_input)) == 5


def test_part2():
    test_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
    d = Day5(content="test")
    assert d.part2(d.parse_content(test_input)) == 12


def test_actual_input():
    with open('./tests/aoc_2021/data/2021day5.txt', 'r') as file:
        content = file.read().strip()
    d = Day5(content="test")
    assert d.part1(d.parse_content(content)) == 4745
    assert d.part2(d.parse_content(content)) == 18442
