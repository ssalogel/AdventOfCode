from src.AoC2016.Day7 import Day7
import pytest


@pytest.mark.parametrize("test_input,expected", [
    ("abba[mnop]qrst", True),
    ("abcd[bddb]xyyx", False),
    ("ioxxoj[asdfgh]zxcvbn", True),
    ("aaaa[qwer]tyui", False)
])
def test_part1(test_input, expected):
    d = Day7(content="test")
    assert d.part1(d.parse_content(test_input)) == expected


@pytest.mark.parametrize("test_input,expected", [
    (["aba", "xyz"], {'aba'}),
    (["xyx", "xyx"], {"xyx"}),
    (["aaa", "eke"], {"eke"}),
    (["zazbz", "cbd"], {"zaz", "zbz"}),
])
def test_get_aba(test_input, expected):
    assert Day7(content="test").get_aba(test_input) == expected


@pytest.mark.parametrize("test_input, babs,expected", [
    (["bab"], {'aba'}, True),
    (["xyx"], {"xyx"}, False),
    (["kek"], {"eke"}, True),
    (["bzb"],  {"zaz", "zbz"}, True)
])
def test_check_bab(test_input, babs, expected):
    assert Day7(content="test").check_bab(test_input, babs) == expected


def test_actual_input():
    with open('./tests/aoc_2016/data/2016day7.txt', 'r') as file:
        content = file.read().strip()
    d = Day7(content="test")
    assert d.part1(d.parse_content(content)) == 118
    assert d.part2(d.parse_content(content)) == 260
