from AoC2015.Day25 import Day25


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day25.txt', 'r') as file:
        content = file.read().strip()
    assert Day25(content=content).part1() == 8997277
    assert Day25(content=content).part2() == "WINNER!"
