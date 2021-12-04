from AoC2015.Day12 import Day12
import pytest


@pytest.mark.parametrize("test_input,expected", [
    ("[1,2,3]", 6),
    ('{"a":2,"b":4}', 6),
    ('[[[3]]]', 3),
    ('{"a":{"b":4},"c":-1}', 3),
    ('{"a":[-1,1]}', 0),
    ('[-1,{"a":1}]', 0),
    ('[]', 0),
    ('{}', 0)
])
def test_part1(test_input, expected):
    d = Day12(content="test")
    assert d.part1(d.parse_content(test_input)) == expected


@pytest.mark.parametrize("test_input,expected", [
    ("[1,2,3]", 6),
    ('{"a":2,"b":4}', 6),
    ('[1,{"c":"red","b":2},3]', 4),
    ('[[[3]]]', 3),
    ('{"a":{"b":4},"c":-1}', 3),
    ('{"d":"red","e":[1,2,3,4],"f":5}', 0),
    ('{"a":[-1,1]}', 0),
    ('[-1,{"a":1}]', 0),
    ('[1,"red",5] ', 6),
    ('[]', 0),
    ('{}', 0)
])
def test_part2(test_input, expected):
    d = Day12(content="test")
    assert d.part2(d.parse_content(test_input)) == expected


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day12.txt', 'r') as file:
        content = file.read().strip()
    d = Day12(content="test")
    assert d.part1(d.parse_content(content)) == 111754
    assert d.part2(d.parse_content(content)) == 65402
