from src.AoC2021.Day14 import Day14


def test_part1():
    test_input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
    d = Day14(content="test")
    assert d.part1(d.parse_content(test_input)) == 1588


def test_part2():
    test_input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
    d = Day14(content="test")
    assert d.part2(d.parse_content(test_input)) == 2188189693529


def test_actual_input():
    with open('./tests/aoc_2021/data/2021day14.txt', 'r') as file:
        content = file.read().strip()
    d = Day14(content="test")
    assert d.part1(d.parse_content(content)) == 2233
    assert d.part2(d.parse_content(content)) == 2884513602164
