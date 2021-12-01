from AoC2016.Day8 import Day8


def test_part1():
    content = """rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1"""
    assert Day8(content=content).part1() == 6


def test_actual_input():
    with open('./tests/aoc_2016/data/2016day8.txt', 'r') as file:
        content = file.read().strip()
    assert Day8(content=content).part1() == 106
