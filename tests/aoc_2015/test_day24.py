from AoC2015.Day24 import Day24


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day24.txt', 'r') as file:
        content = file.read().strip()
    assert Day24(content=content).part1() == 10723906903
    assert Day24(content=content).part2() == 74850409
