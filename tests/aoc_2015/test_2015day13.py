from src.AoC2015.Day13 import Day13


def test_part1():
    content = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""
    d = Day13(content="test")
    assert d.part1(d.parse_content(content)) == 330


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day13.txt', 'r') as file:
        content = file.read().strip()
    d = Day13(content="test")
    assert d.part1(d.parse_content(content)) == 618
    assert d.part2(d.parse_content(content)) == 601
