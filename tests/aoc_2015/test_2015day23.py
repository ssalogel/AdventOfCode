from AoC2015.Day23 import Day23


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day23.txt', 'r') as file:
        content = file.read().strip()
    assert Day23(content=content).part1() == 307
    assert Day23(content=content).part2() == 160
