from AoC2021.Day6 import Day6


def test_spawn_fishes():
    d = Day6(content="test")
    assert sum(d.spawn_fishes([0, 1, 1, 2, 1, 0, 0, 0, 0], 18)) == 26


def test_part1():
    test_input = """3,4,3,1,2"""
    d = Day6(content="test")
    assert d.part1(d.parse_content(test_input)) == 5934


def test_part2():
    test_input = """3,4,3,1,2"""
    d = Day6(content="test")
    assert d.part2(d.parse_content(test_input)) == 26984457539


def test_actual_input():
    with open('./tests/aoc_2021/data/2021day6.txt', 'r') as file:
        content = file.read().strip()
    d = Day6(content="test")
    assert d.part1(d.parse_content(content)) == 387413
    assert d.part2(d.parse_content(content)) == 1738377086345
