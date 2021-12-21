from src.AoC2015.Day11 import Day11
import pytest


def pass_to_num(string: str) -> list[int]:
    return list(map(ord, string))


@pytest.mark.parametrize("test_input,expected", [
    ('hijklmmn', True),
    ('abbceffg', False),
])
def test_has_three_sequence(test_input, expected):
    assert Day11(content='test').has_three_sequence(pass_to_num(test_input)) == expected


@pytest.mark.parametrize("test_input,expected", [
    ('hijklmmn', False),
    ('abbceffg', True),
    ('abbcegjk', True)
])
def test_no_forbidden(test_input, expected):
    assert Day11(content='test').no_forbidden(pass_to_num(test_input)) == expected


@pytest.mark.parametrize("test_input,expected", [
    ('hijklmmn', False),
    ('abbceffg', True),
    ('abbcegjk', False)
])
def test_has_double(test_input, expected):
    assert Day11(content='test').has_double(pass_to_num(test_input)) == expected


@pytest.mark.parametrize("test_input,expected", [
    ('abcdefgh', 'abcdffaa'),
    ('ghijklmn', 'ghjaabcc'),
])
def test_get_next_valid_pass(test_input, expected):
    assert Day11(content='test').get_next_valid_pass(pass_to_num(test_input)) == pass_to_num(expected)


def test_actual_input():
    with open('./tests/aoc_2015/data/2015day11.txt', 'r') as file:
        content = file.read().strip()
    d = Day11(content="test")
    assert d.part1(d.parse_content(content)) == "hxbxxyzz"
    assert d.part2(d.parse_content(content)) == "hxcaabcc"
