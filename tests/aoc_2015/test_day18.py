from AoC2015.Day18 import Day18


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day18.txt', 'r') as file:
        content = file.read().strip()
    assert Day18(content=content).part1() == 1061
    assert Day18(content=content).part2() == 1006
