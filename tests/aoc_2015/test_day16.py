from AoC2015.Day16 import Day16


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day16.txt', 'r') as file:
        content = file.read().strip()
    assert Day16(content=content).part1() == '103'
    assert Day16(content=content).part2() == '405'
