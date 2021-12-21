from src.AoC2021.Day9 import Day9


def test_find_low_points():
    d = Day9(content="test")
    test_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""
    assert d.find_low_points(d.parse_content(test_input)) == ([(0, 1), (0, 9), (2, 2), (4, 6)], [1, 0, 5, 5])


def test_part1():
    test_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""
    d = Day9(content="test")
    assert d.part1(d.parse_content(test_input)) == 15


def test_part2():
    test_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""
    d = Day9(content="test")
    assert d.part2(d.parse_content(test_input)) == 1134


def test_actual_input():
    with open('./tests/aoc_2021/data/2021day9.txt', 'r') as file:
        content = file.read().strip()
    d = Day9(content="test")
    assert d.part1(d.parse_content(content)) == 456
    assert d.part2(d.parse_content(content)) == 1047744
