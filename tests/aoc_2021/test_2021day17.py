from src.AoC2021.Day17 import Day17


def test_part1():
    content = 'target area: x=20..30, y=-10..-5'
    d = Day17(content=content)
    assert d.part1(d.parse_content(d.content)) == 45


def test_part2():
    content = 'target area: x=20..30, y=-10..-5'
    d = Day17(content=content)
    assert d.part2(d.parse_content(d.content)) == 112


def test_actual_input():
    with open('./tests/aoc_2021/data/2021day17.txt', 'r') as file:
        content = file.read().strip()
    d = Day17(content="test")
    assert d.part1(d.parse_content(content)) == 4278
    assert d.part2(d.parse_content(content)) == 1994
