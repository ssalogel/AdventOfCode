from AoC2016.Day3 import Day3


def test_actual_input():
    with open('./tests/aoc_2016/data/2016day3.txt', 'r') as file:
        content = file.read().strip()
    assert Day3(content=content).part1() == 1050
    assert Day3(content=content).part2() == 1921
