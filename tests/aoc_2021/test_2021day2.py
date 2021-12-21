from src.AoC2021.Day2 import Day2


def test_part1():
    test_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
    d = Day2(content="test")
    assert d.part1(d.parse_content(test_input)) == 150


def test_part2():
    test_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
    d = Day2(content="test")
    assert d.part2(d.parse_content(test_input)) == 900


def test_actual_input():
    with open('./tests/aoc_2021/data/2021day2.txt', 'r') as file:
        content = file.read().strip()
    d = Day2(content="test")
    assert d.part1(d.parse_content(content)) == 2272262
    assert d.part2(d.parse_content(content)) == 2134882034
