from src.AoC2021.Day7 import Day7


def test_part1():
    test_input = """16,1,2,0,4,2,7,1,2,14"""
    d = Day7(content="test")
    assert d.part1(d.parse_content(test_input)) == 37


def test_part2():
    test_input = """16,1,2,0,4,2,7,1,2,14"""
    d = Day7(content="test")
    assert d.part2(d.parse_content(test_input)) == 168


def test_actual_input():
    with open('./tests/aoc_2021/data/2021day7.txt', 'r') as file:
        content = file.read().strip()
    d = Day7(content="test")
    assert d.part1(d.parse_content(content)) == 344535
    assert d.part2(d.parse_content(content)) == 95581659
