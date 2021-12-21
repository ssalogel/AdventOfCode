from src.AoC2021.Day12 import Day12
import pytest


test_input_1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

test_input_2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

test_input_3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""


@pytest.mark.parametrize("test_input,expected", [
    (test_input_1, 10),
    (test_input_2, 19),
    (test_input_3, 226)
])
def test_part1(test_input, expected):
    d = Day12(content="test")
    assert d.part1(d.parse_content(test_input)) == expected


@pytest.mark.parametrize("test_input,expected", [
    (test_input_1, 36),
    (test_input_2, 103),
    (test_input_3, 3509)
])
def test_part2(test_input, expected):
    d = Day12(content="test")
    assert d.part2(d.parse_content(test_input)) == expected


def test_actual_input():
    with open('./tests/aoc_2021/data/2021day12.txt', 'r') as file:
        content = file.read().strip()
    d = Day12(content="test")
    assert d.part1(d.parse_content(content)) == 3761
    assert d.part2(d.parse_content(content)) == 99138
