from AoC2016.Day10 import Day10


def test_actual_input():
    with open('./tests/aoc_2016/data/2016day10.txt', 'r') as file:
        content = file.read().strip()
    assert Day10(content=content).part1() == 98
    assert Day10(content=content).part2() == 4042
