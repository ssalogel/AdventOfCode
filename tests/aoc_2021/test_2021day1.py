from src.AoC2021.Day1 import Day1


def test_part1():
    test_input = """199
200
208
210
200
207
240
269
260
263"""
    d = Day1(content="test")
    assert d.part1(d.parse_content(test_input)) == 7


def test_part2():
    test_input = """199
200
208
210
200
207
240
269
260
263"""
    d = Day1(content="test")
    assert d.part2(d.parse_content(test_input)) == 5


def test_actual_input():
    with open('./tests/aoc_2021/data/2021day1.txt', 'r') as file:
        content = file.read().strip()
    d = Day1(content="test")
    assert d.part1(d.parse_content(content)) == 1715
    assert d.part2(d.parse_content(content)) == 1739
