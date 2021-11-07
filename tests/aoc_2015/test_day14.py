from AoC2015.Day14 import Day14


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day14.txt', 'r') as file:
        content = file.read().strip()
    assert Day14(content=content).part1() == 2655
    assert Day14(content=content).part2() == 1059
