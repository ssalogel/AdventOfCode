from AoC2015.Day6 import Day6


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day6.txt', 'r') as file:
        content = file.read().strip()
    assert Day6(content=content).part1() == 569999
    assert Day6(content=content).part2() == 17836115
