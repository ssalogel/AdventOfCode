from AoC2015.Day22 import Day22


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day22.txt', 'r') as file:
        content = file.read().strip()
    assert Day22(content=content).part1() == 953
    assert Day22(content=content).part2() == 1289
