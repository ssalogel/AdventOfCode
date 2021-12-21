from src.AoC2021.Day15 import Day15


def test_part1():
    test_input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""
    d = Day15(content="test")
    assert d.part1(d.parse_content(test_input)) == 40


def test_part2():
    test_input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""
    d = Day15(content="test")
    assert d.part2(d.parse_content(test_input)) == 315

def test_actual_input():
    with open('./tests/aoc_2021/data/2021day15.txt', 'r') as file:
        content = file.read().strip()
    d = Day15(content="test")
    assert d.part1(d.parse_content(content)) == 720
    assert d.part2(d.parse_content(content)) == 3025
